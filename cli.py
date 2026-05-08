import argparse

from bot.client import get_client
from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import setup_logger


def print_response(response):
    print("\n========= ORDER RESPONSE =========")

    print(f"Order ID      : {response.get('orderId')}")
    print(f"Status        : {response.get('status')}")
    print(f"Executed Qty  : {response.get('executedQty')}")
    print(f"Average Price : {response.get('avgPrice', 'N/A')}")

    print("\nSUCCESS: Order placed successfully.")


def main():
    setup_logger()

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True, help="Trading pair")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        symbol = args.symbol.upper()
        side = args.side.upper()
        order_type = args.type.upper()
        quantity = args.quantity
        price = args.price

        # Validation
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(order_type, price)

        print("\n========= ORDER REQUEST =========")
        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : {order_type}")
        print(f"Quantity : {quantity}")

        if order_type == "LIMIT":
            print(f"Price    : {price}")

        client = get_client()

        if order_type == "MARKET":
            response = place_market_order(
                client,
                symbol,
                side,
                quantity
            )

        else:
            response = place_limit_order(
                client,
                symbol,
                side,
                quantity,
                price
            )

        print_response(response)

    except ValueError as e:
        print(f"\nVALIDATION ERROR: {e}")

    except Exception as e:
        print(f"\nERROR: {e}")


if __name__ == "__main__":
    main()