'''
Этап 1. Проблемная версия приложения (намеренные нарушения SOLID).

Нарушения:
1. SRP  - класс TicketService отвечает сразу за хранение, оплату,
          уведомления и вывод в консоль.
2. OCP  - способ оплаты выбирается через if/elif; новый способ
          требует изменения метода buy().
3. DIP  - хранилище (список) жёстко задано внутри класса.
4. ISP  - класс TicketManager содержит методы, которые нужны не всем клиентам.
5. LSP  - SeasonTicket наследует Ticket, но ломает метод refund().
'''


class Ticket:
    def __init__(self, passenger, train, seat, price):
        self.passenger = passenger
        self.train = train
        self.seat = seat
        self.price = price
        self.status = "забронирован"

    def refund(self):
        self.status = "возвращён"


class SeasonTicket(Ticket):            # нарушение LSP
    def refund(self):
        raise NotImplementedError("Абонемент вернуть нельзя")


class TicketService:                   # нарушение SRP и DIP
    def __init__(self):
        self.tickets = []              # хранилище жёстко внутри класса

    def buy(self, passenger, train, seat, price, payment_type):
        ticket = Ticket(passenger, train, seat, price)
        self.tickets.append(ticket)
        # нарушение OCP - новый способ оплаты требует правки метода
        if payment_type == "card":
            print(f"Оплата картой: {price}")
        elif payment_type == "cash":
            print(f"Оплата наличными: {price}")
        elif payment_type == "transfer":
            print(f"Оплата переводом: {price}")
        else:
            print("Неизвестный способ оплаты")
        ticket.status = "оплачен"
        print(f"Билет для {passenger} оформлен")              # UI внутри сервиса
        print(f"[EMAIL] Уведомление отправлено {passenger}")  # уведомление внутри сервиса
        return ticket


class TicketManager:                   # нарушение ISP - слишком большой интерфейс
    def add(self): ...
    def remove(self): ...
    def get(self): ...
    def print_report(self): ...
    def send_email(self): ...
    def send_sms(self): ...
    def export_pdf(self): ...


if __name__ == "__main__":
    service = TicketService()
    service.buy("Иванов И.И.", "001А", 5, 2500, "card")
