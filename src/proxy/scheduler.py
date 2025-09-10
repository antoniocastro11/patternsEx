import asyncio
from proxy.client import Api
from proxy.observer import metrics

class AskScheduler:
    _instance = None

    def __init__(self):
        self.queue = asyncio.Queue()
        self.client = Api()
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
        print("Iniciando _run()...")
        while True:
            print("Aguardando item na fila...")
            cmd, future = await self.queue.get()
            try:
                print("Executando comando...")
                result = await cmd.execute(self.client)
                future.set_result(result)
                metrics.notify("success")
            except Exception as e:
                future.set_exception(e)
                metrics.notify("error")
            await asyncio.sleep(1)
