from Order import Order

class Buy_Order(Order):
    
    def sort(self, index, buy):
        """
        This function performs a sorting of the buy pending orders in order of priority

        index: Index at which to add in the market order since market orders always get fulfilled first
        buy: Mapping of the buy pending orders
        return: null
        """
        
        stock = self.getStock()
        if stock not in index:
            index[stock] = 1 # One order in the buy pending orders
        # Check if stock is in the queue
        if stock not in buy:
            buy[stock] = [self]
        else:
            # Check if stock is market or limit order
            arr = buy[stock]
            if self.getType() == "MKT":
                arr.insert(index[stock], self)
                index[stock] +=  1
            else:
                status = False
                # Sorting based on the 'buy' priority mentioned above
                
                for i in range(index[stock], len(arr)):
                    
                    if self.getPrice() > arr[i].getPrice():
                        arr.insert(i, self)
                        status = True
                        break
                if not status:
                    arr.append(self)
        return index

            
        