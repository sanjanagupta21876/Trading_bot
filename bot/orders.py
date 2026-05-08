from binance.exceptions import BinanceAPIException
import logging

logger = logging.getLogger()


def place_market_order(client, symbol, side, quantity):
    try:
        logger.info(
            f"MARKET ORDER REQUEST | Symbol={symbol} Side={side} Quantity={quantity}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(f"MARKET ORDER RESPONSE | {response}")

        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        raise

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise


def place_limit_order(client, symbol, side, quantity, price):
    try:
        logger.info(
            f"LIMIT ORDER REQUEST | Symbol={symbol} Side={side} Quantity={quantity} Price={price}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(f"LIMIT ORDER RESPONSE | {response}")

        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        raise

    except Exception as e:
        logger.error(f"FULL ERROR: {repr(e)}")
        raise