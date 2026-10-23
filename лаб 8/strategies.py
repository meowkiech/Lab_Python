# Strategy: взаимозаменяемые алгоритмы расчёта цены билета


class StandardPricing:
    def calculate(self, base_price: float) -> float:
        return base_price


class DiscountPricing:          # льготный тариф
    def calculate(self, base_price: float) -> float:
        return base_price * 0.5


class DynamicPricing:           # динамический тариф зависит от загрузки
    def __init__(self, load_factor: float = 0.3) -> None:
        self.load_factor = load_factor

    def calculate(self, base_price: float) -> float:
        return base_price * (1 + self.load_factor)
