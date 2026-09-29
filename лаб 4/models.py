
import exceptions

class Dish:
    def __init__(self, name, category, price, caloric):
        self.__name = name
        self.__category = category
        self.price = price
        self.__caloric = caloric

    @property
    def name(self):
        return self.__name

    @property
    def category(self):
        return self.__category

    @property
    def caloric(self):
        return self.__caloric

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise exceptions.FuckingLessZeroPrice()
        self.__price = new_price

class Order:
    def __init__(self, names, customer_name):
        self.__names = names
        self.__customer_name = customer_name
        self.__price = 0
        self.status = False

    @property
    def price(self):
        return self.__price

    @property
    def names(self):
        return self.__names

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise exceptions.FuckingLessZeroPrice()
        else:
            self.__price = new_price

    def order_done(self):
        print('Заказ успешно оформлен!')
        self.status = True
