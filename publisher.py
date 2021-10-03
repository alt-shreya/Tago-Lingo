class Publisher:
    def __init__(self) -> None:
        self.subs = []

    def subscribe(self, subscriber):
        self.subs.append(subscriber)

    def unsubscribe(self, subscriber):
        if self.subs.__contains__(subscriber):
            self.subs.remove(subscriber)

    async def publish(self, msg):
        for sub in self.subs:
            await sub.send_to_clients(msg)
