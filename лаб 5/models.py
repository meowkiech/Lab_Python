class Dish:
    def __init__(self, name, category, price, caloric):
        self.name = name
        self.category = category
        self.price = float(price)
        self.caloric = float(caloric)

class VeggieDish(Dish):
    def __init__(self, name, category, price, caloric):
        super().__init__(name, category, price, caloric)
        self.is_veggie = True

class MeatDish(Dish):
    def __init__(self, name, category, price, caloric):
        super().__init__(name, category, price, caloric)
        self.is_veggie = False