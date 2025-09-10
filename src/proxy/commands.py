class AskCommand:
    async def execute(self, client):
        raise NotImplementedError


class ScoreAskCommand(AskCommand):
    def __init__(self, param):
        self.param = param

    async def execute(self, client):
        return await client.get_score(self.param)