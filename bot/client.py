from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")


def get_client():

    client = Client(
        API_KEY,
        API_SECRET,
        testnet=True,
        requests_params={
            "timeout": 20
        }
    )

    # Futures Testnet URL
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client