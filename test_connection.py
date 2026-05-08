from bot.client import get_client

client = get_client()

try:

    ping = client.ping()

    print("Connection Successful")
    print(ping)

except Exception as e:

    print("ERROR:")
    print(e)