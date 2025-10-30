class Product:
    def __init__(self, product_type, name, price):
        self.type = product_type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = {}  # {product_name: {'product': Product, 'amount': int, 'discount': float}}
        self.income = 0

    def add(self, product, amount):
        """Adds product with 30% price premium"""
        if amount <= 0:
            raise ValueError("Amount must be positive")

        price_with_premium = product.price * 1.3

        if product.name in self.products:
            self.products[product.name]['amount'] += amount
        else:
            self.products[product.name] = {
                'product': Product(product.type, product.name, price_with_premium),
                'amount': amount,
                'discount': 0
            }

    def set_discount(self, identifier, percent, identifier_type='name'):
        """Sets discount for products by name or type"""
        if percent < 0 or percent > 100:
            raise ValueError("Discount must be between 0 and 100")

        for name, data in self.products.items():
            if identifier_type == 'name' and name == identifier:
                data['discount'] = percent
            elif identifier_type == 'type' and data['product'].type == identifier:
                data['discount'] = percent

    def sell_product(self, product_name, amount):
        """Sells product and increases income"""
        if product_name not in self.products:
            raise ValueError(f"Product {product_name} not found")

        if self.products[product_name]['amount'] < amount:
            raise ValueError(f"Not enough {product_name} in stock")

        product_data = self.products[product_name]
        price = product_data['product'].price
        discount = product_data['discount']
        final_price = price * (1 - discount / 100)

        self.products[product_name]['amount'] -= amount
        self.income += final_price * amount

    def get_income(self):
        """Returns total income"""
        return self.income

    def get_all_products(self):
        """Returns info about all products"""
        result = []
        for name, data in self.products.items():
            result.append({
                'name': name,
                'type': data['product'].type,
                'amount': data['amount'],
                'price': data['product'].price,
                'discount': data['discount']
            })
        return result

    def get_product_info(self, product_name):
        """Returns tuple with product name and amount"""
        if product_name not in self.products:
            raise ValueError(f"Product {product_name} not found")
        return (product_name, self.products[product_name]['amount'])


# Тестування
p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)
assert s.get_product_info('Ramen') == ('Ramen', 290)