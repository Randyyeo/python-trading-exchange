# Trading Exchange

This is a trading program created using python programming. It uses an object oriented approach to easily create new functions to the application. 
Right now, this application can handle limit, market orders and it can display your bid, ask and last prices for each individual stock. 
It doesn't connect to any API to gather stock information, but that will be part of any future updates to the application


## Installation

Clone our repository or download the zip file.

```bash
git clone https://github.com/Randyyeo/python-trading-exchange.git
```

Go to the folder of the files in your local and use the package manager npm to install the relevant dependencies.

```bash
cd python-trading-exchange
```

## Running the Application 

```bash
python app.py
```

## Specific commands

1. Buy/Sell Stocks
(Limit)
```bash
BUY FB LMT $20.00 20
```
(Market)
```bash
BUY FB MKT 20
```
Swap 'BUY' with 'SELL' to indicate a selling order

2. View Orders
```bash
VIEW ORDERS
```

3. Quoting Stocks
```bash
QUOTE FB
```
