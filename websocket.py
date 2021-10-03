import asyncio
import logging
from asyncio.streams import start_server
from time import sleep

import websockets
from websockets import WebSocketServerProtocol

from camera_detector import Detector
from publisher import Publisher

logging.basicConfig(level=logging.INFO)


class Server:
    clients = set()

    async def register(self, ws: WebSocketServerProtocol):
        self.clients.add(ws)
        logging.info(f"{ws.remote_address} connects.")

    async def unregister(self, ws: WebSocketServerProtocol):
        self.clients.remove(ws)
        logging.info(f"{ws.remote_address} disconnects.")

    async def send_to_clients(self, message: str):
        if self.clients:
            await asyncio.wait(
                [client.send(message) for client in self.clients]
            )

    async def ws_handler(self, ws: WebSocketServerProtocol, uri: str):
        await self.register(ws)
        messageChannel = Publisher()
        messageChannel.subscribe(self)
        detector = Detector(messageChannel)
        await detector.run_camera()
        try:
            await self.distribute(ws)
        finally:
            await self.unregister(ws)

    async def distribute(self, ws: WebSocketServerProtocol):
        async for message in ws:
            await self.send_to_clients(message)
            print(message)
            if message == "hand gestures":
                # start tracking the users hand gestures
                print("hand gestures")


if __name__ == "__main__":
    server = Server()
    start_server = websockets.serve(server.ws_handler, "localhost", 4000)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server)
    loop.run_forever()
