import httpx

class Api:
    BaseURL = "https://score.hsborges.dev"

    async def get_score(self, param):
        async with httpx.AsyncClient() as client:
            r = await cliente.get(f"{self.BaseURL}/score", param = {"param" : param})
            return r.json()
