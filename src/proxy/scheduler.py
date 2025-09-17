import asyncio
import time
from proxy.client import Api
from proxy.observer import metrics

class AskScheduler:
    _instance = None

    def __init__(self):
        self.queue = asyncio.Queue()
        self.client = Api()
        self.last_request_time = None
        asyncio.create_task(self._run())

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = AskScheduler()
        return cls._instance

    
    async def enqueue(self, command):
        loop = asyncio.get_event_loop()
        future = loop.create_future()
        await self.queue.put((command, future))
        return future
    
    async def _run(self):
        while True:
            cmd, future = await self.queue.get()
            print(f"Executando requisição às {time.strftime('%H:%M:%S')}")
            
            now = time.time()
            if self.last_request_time is not None:
                elapsed = now - self.last_request_time
                wait_time = max(0, 1 - elapsed)
                if wait_time > 0:
                    await asyncio.sleep(wait_time)

            try:
                result = await cmd.execute(self.client)
                future.set_result(result)
                metrics.notify("success")
            except Exception as e:
                future.set_exception(e)
                metrics.notify("error")

            self.last_request_time = time.time()