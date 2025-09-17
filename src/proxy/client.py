import httpx
import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Api:
    BaseURL = getenv("API_URL")

    async def get_score(self, cpf: str):
        headers = {
            "client-id": "12345"
        }
        params = {
            "cpf": cpf
        }
        async with httpx.AsyncClient() as client:
            r = await client.get(f"{self.BaseURL}/score", params=params, headers=headers)
            r.raise_for_status()
            return r.json()