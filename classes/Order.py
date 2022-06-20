class Order:
    def __init__(self, action, stock, type, price, amount):
        self.action = action
        self.stock = stock
        self.type = type
        self.price = price
        self.amount = amount 
        self.current = 0
        self.status = "PENDING"

    # Printing out the order placed
    def view(self):
        if self.price == None:
            return f"{self.action} {self.stock} {self.type} {self.current}/{self.amount} {self.status}"
        else:
            dot_index = str(self.price).index(".")
            if len(str(self.price)[dot_index+1:]) == 1:
                return f"{self.action} {self.stock} {self.type} ${str(self.price)}0 {self.current}/{self.amount} {self.status}"
            else:
                return f"{self.action} {self.stock} {self.type} ${str(self.price)} {self.current}/{self.amount} {self.status}"

    def getCurrent(self):
        return self.current

    def setCurrent(self, result):
        self.current += result
        if self.current == self.amount:
            self.status = "FILLED"
        elif self.current > 0:
            self.status = "PARTIAL"
        
    def getRemaining(self):
        return self.amount - self.current

    def getPrice(self):
        return self.price

    def getType(self):
        return self.type

    def getStatus(self):
        return self.status
    
    def setPrice(self, result):
        self.price = result

    def getStock(self):
        return self.stock
