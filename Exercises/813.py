class Shop():
    def __init__(self, shop_name, store_type, number_of_units = 0):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = number_of_units

    def describe_shop(self):
        print(f"{self.shop_name} / {self.store_type}")

    @staticmethod
    def open_shop():
        print('The store is open')

    def set_number_of_units(self, n):
        self.number_of_units = n

    def increvent_number_of_units(self, n):
        self.number_of_units += n


class Discount(Shop):
    def __init__(self, shop_name, store_type, discount_products = 0, number_of_units = 0):
        super().__init__(shop_name, store_type, number_of_units)
        self.discount_products = discount_products


    def get_discount_products(self):
        if self.discount_products == 0:
            return []
        return[self.discount_products]


store = Shop("Rozetka", "Electronics")
print(store.shop_name)
print(store.store_type)
store.describe_shop()
store.open_shop()
print(store.number_of_units)
store.number_of_units = 3000000
print(store.number_of_units)
store.number_of_units = 987
print(store.number_of_units)

print('-' * 30)

store2 = Shop("eva", "Cosmetics")
store2.describe_shop()
store2.set_number_of_units(123)
print(store2.number_of_units)
store2.increvent_number_of_units(57)
print(store2.number_of_units)

print('-' * 30)


discount_items = ['Samsung S23', 'Aser Laptop 14"']
store_discount = Discount('Comfy', 'Tecnics', discount_items)
store_discount.discount_products = ['TV', "Smartphones", "Laptops"]
print(store_discount.discount_products)

store_discount2 = Discount('Avrora', "Home")
print(store_discount2.__dict__)
print(store_discount2.discount_products)