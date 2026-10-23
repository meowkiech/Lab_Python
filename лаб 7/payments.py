from interfaces import PaymentMethod

class CardPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Оплата картой: {amount} руб.")

class CashPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Оплата наличными: {amount} руб.")

class BankTransfer(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Оплата банковским переводом: {amount} руб.")
