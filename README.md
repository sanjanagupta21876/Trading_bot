# Binance Futures Testnet Trading Bot

A simplified Python trading bot for Binance Futures Testnet (USDT-M). This bot allows you to easily place market and limit orders via a Command Line Interface (CLI).

## Features

- MARKET orders
- LIMIT orders
- BUY and SELL support
- CLI interface
- Logging
- Error handling
- Input validation

## Prerequisites

- Python 3.7+
- A Binance Futures Testnet account (with API Key and Secret)

## Setup

### 1. Clone Repository

```bash
git clone <your_repo_url>
cd trading_bot
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configuration

Create a `.env` file in the root directory (you can copy `.env.example` if it exists) and add your Binance Testnet API credentials:

```ini
BINANCE_API_KEY=your_testnet_api_key_here
BINANCE_API_SECRET=your_testnet_api_secret_here
```

### 5. Quick Start Flow

Run the following commands in order to verify your setup and make your first testnet trade:

```bash
python test_connection.py
python test_balance.py
```

## Usage

You can interact with the bot using `cli.py`. 

### Command Line Arguments

- `--symbol`: Trading pair (e.g., BTCUSDT, ETHUSDT). Required.
- `--side`: BUY or SELL. Required.
- `--type`: MARKET or LIMIT. Required.
- `--quantity`: Order quantity in base asset. Required.
- `--price`: Order price (required if `--type` is LIMIT).

### Examples

**Place a Market Buy Order:**
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

**Place a Market Sell Order:**
```bash
python cli.py --symbol ETHUSDT --side SELL --type MARKET --quantity 0.5
```

**Place a Limit Buy Order:**
```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 60000
```

## Testing

To run the connection tests or check balance:
```bash
python test_connection.py
python test_balance.py
python test.py
```

## Disclaimer

This is a testnet bot for educational/testing purposes. Do not use this with real funds without proper testing, risk management, and understanding of the Binance API.