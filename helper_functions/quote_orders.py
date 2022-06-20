def quote_orders(stock, buy, mkt_buy_index, sell, mkt_sell_index, last):
    if stock in buy and len(buy[stock]) != 0:
        if len(buy[stock]) > mkt_buy_index[stock]:
            bid_price = float(buy[stock][mkt_buy_index[stock]].getPrice())
        else:
            if len(buy[stock]) == mkt_buy_index[stock] and buy[stock][mkt_buy_index[stock]-1].getType() == "LMT":
                bid_price = float(buy[stock][mkt_buy_index[stock]].getPrice())
            else:
                bid_price = "0.00"
    else:
        bid_price = "0.00"

    if stock in sell and len(sell[stock]) != 0:
        if len(sell[stock]) > mkt_sell_index[stock]:
            ask_price = float(sell[stock][mkt_sell_index[stock]].getPrice())
        else:
            if len(sell[stock]) == mkt_sell_index[stock] and sell[stock][mkt_sell_index[stock]-1].getType() == "LMT":
                ask_price = float(buy[stock][mkt_sell_index[stock]].getPrice())
            else:
                ask_price = "0.00"
    else:
        ask_price = "0.00"

    if stock in last:
        last_price = float(last[stock])
    else:
        last_price = "0.00"

    return (bid_price, ask_price, last_price)