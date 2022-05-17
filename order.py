class Order:
    """
    Represents order to be managed by manager class.
    """
    
    def __init__(self, id: int, name: str, price: float):
        self.id: int = id
        self.name: str = name
        self.price: float = price  # for now, decimal would be used normally
    
    def __str__(self):
        return "id:{}, name:{}, price:{}".format(self.id, self.name, self.price)
    
    def __eq__(self, other):
        # only id was mentioned as hash
        return self.id == other.id
        
    def __hash__(self):
        # only id was mentioned as hash
        return hash(self.id)


if __name__ == "__main__":
    
    order_1 = Order(1, "jacek", 10)
    order_2 = Order(1, "jacek2", 12)
    
    orders = {}
    orders[order_1] = 1
       
    print(order_2 in orders)
    
    orders[order_2] += 1
    
    print(orders)