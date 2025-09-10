from fastapi import FastAPI
from proxy.scheduler import AskScheduler
from proxy.commands import ScoreAskCommand
from proxy.observer import metrics

app = FastAPI()
scheduler = AskScheduler.get_instance()

@app.get("/proxy/score")
async def proxy_score(param: str):
    cmd = ScoreAskCommand(param)
    future = await scheduler.enqueue(cmd)
    result = await future
    return result

@app.get("/metrics")
def get_metrics():
    return metrics.get_metrics()

@app.get("/health")
def health():
    return {"status": "ok"}
