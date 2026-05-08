from bot.client import get_client

client = get_client()

try:

    balances = client.futures_account_balance()

    print(balances)

except Exception as e:

    print(e)