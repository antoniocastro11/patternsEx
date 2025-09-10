import httpx

class Api:
    BaseURL = "https://score.hsborges.dev/api"

    async def get_score(self, cpf: str):
        params = {
            "cpf": cpf
        }
        async with httpx.AsyncClient() as client:
            r = await client.get(f"{self.BaseURL}/score", params=params)
            r.raise_for_status()
            return r.json()