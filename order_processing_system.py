class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.name = product_name
        self.price = price


class Order:
    def __init__(self, order_id, products):
        self.order_id = order_id
        self.products = products


class OrderProcessingSystem:
    def __init__(self):
        self.products = []
        self.orders = []

    def add_product(self, product_id, name, price):
        self.products.append(Product(product_id, name, price))
        print(f"Product '{name}' added.")

    def remove_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                print(f"Product with ID {product_id} removed.")
                return
        print(f"Product with ID {product_id} not found.")

    def place_order(self, order_id, product_ids):
        ordered_products = []
        for product_id in product_ids:
            try:
                product = next(product for product in self.products if product.product_id == product_id)
                ordered_products.append(product)
            except StopIteration:
                print(f"Product with ID {product_id} not found. Order not placed.")
                return

        self.orders.append(Order(order_id, ordered_products))
        print(f"Order with ID {order_id} placed successfully.")

    def cancel_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                self.orders.remove(order)
                print(f"Order with ID {order_id} cancelled.")
                return
        print(f"Order with ID {order_id} not found.")

    def list_all_products(self):
        for product in self.products:
            print(f"ID: {product.product_id}, Name: {product.name}, Price: {product.price}")

    def list_all_orders(self):
        for order in self.orders:
            print(f"Order ID: {order.order_id}")
            for product in order.products:
                print(f"  Product: {product.name}, Price: {product.price}")


# Example test
system = OrderProcessingSystem()

system.add_product(1, "Apple iPhone 14", 90000)
system.add_product(2, "Samsung TV", 55000)

system.place_order(1, [1, 2])

system.cancel_order(2)

system.list_all_products()
system.list_all_orders()
