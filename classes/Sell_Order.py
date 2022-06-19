from Order import Order

class Sell_Order(Order):
    
    def sort(self, index, sell):
        """
        This function performs a sorting of the sell pending orders in order of priority

        index: Index at which to add in the market order since market orders always get fulfilled first
        buy: Mapping of the sell pending orders
        return: null
        """
        stock = self.getStock()
        # Check if stock has been ordered before
        if stock not in index:
            index[stock] = 1 # one stock in the sell pending orders
        # Check if stock is in the queue
        if stock not in sell:
            sell[stock] = [self]
        else:
            # Check if stock is market or limit order
            arr = sell[stock]
            if self.getType() == "MKT":
                arr.insert(index[stock], self)
                index[stock] +=  1
            else:
                status = False
                # Sorting based on the 'sell' priority mentioned above
                for i in range(index[stock], len(arr)):
                    if self.getPrice() < arr[i].getPrice():
                        status = True
                        arr.insert(i, self)
                        break
                if not status:
                    arr.append(self)
        return index
            
        