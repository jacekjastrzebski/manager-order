
from order import Order


class Manager:
    """
    A class responsible for managing orders.
    """
    
    def __init__(self):
        self.orders = {}
    
    def add_order(self, order: Order):
        if order in self.orders:
            self.orders[order] += 1
        else:
            self.orders[order] = 1

    def remove_order(self, order: Order):
        if self.orders[order] == 0: 
            raise ValueError('Order value already 0 - cannot be deleted.')
        else:
            self.orders[order] -= 1

    def print_orders(self):
        orders = ''
        
        for order, quantity in self.orders.items():
            entry = "Order: {} | Quantity: {}\n".format(order, quantity) 
            orders += entry
        
        print(orders)


if __name__ == "__main__":
    
    order_1 = Order(1, "order_1", 10)
    order_2 = Order(1, "order_1", 12)
    order_3 = Order(2, "order_2", 10)
    order_4 = Order(3, "order_3", 10)
    
    orders_manager = Manager()
    
    orders_manager.add_order(order_1)
    orders_manager.add_order(order_2)
    orders_manager.add_order(order_3)
    orders_manager.add_order(order_4)
    orders_manager.print_orders()
    
    orders_manager.remove_order(order_4)
    orders_manager.remove_order(order_4)
    
