import time

import cv2


class Detector:
    def __init__(self, messageChannel) -> None:
        self.messageChannel = messageChannel

    async def run_camera(self):
        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )
        video = cv2.VideoCapture(0)
        while True:
            await self.messageChannel.publish("idle")

            _, img = video.read()

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

            if not len(faces) == 0:
                await self.run_mascot()
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            cv2.imshow("img", img)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        video.release()

    async def run_mascot(self):
        await self.messageChannel.publish("wake up")
        time.sleep(2)
        await self.messageChannel.publish("introduction")
        time.sleep(5)
        await self.messageChannel.publish("mission")
        time.sleep(5)
        await self.messageChannel.publish("tell joke")
        time.sleep(3)
        await self.messageChannel.publish("just kidding")
        time.sleep(2)
