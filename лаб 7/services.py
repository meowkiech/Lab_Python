from models import Ticket, Train, TicketStatus
from interfaces import PaymentMethod, Notifier

class TicketNotFoundError(Exception):
    pass

class TicketService:
    def __init__(self, repository, notifier: Notifier) -> None:
        self.repository = repository          # DIP: зависимость передаётся извне
        self.notifier = notifier
        self._next_id = 1

    def search_trains(self, trains: list[Train], route: str) -> list[Train]:
        return [t for t in trains if route.lower() in t.route.lower()]

    def book(self, train: Train, passenger: str, seat: int, price: float) -> Ticket:
        ticket = Ticket(self._next_id, passenger, train.number, seat, price)
        self._next_id += 1
        self.repository.add(ticket)
        self.notifier.send(passenger, f"Билет на поезд {train.number} забронирован")
        return ticket

    def buy(self, ticket_id: int, payment: PaymentMethod) -> None:
        ticket = self._get(ticket_id)
        payment.pay(ticket.price)             # OCP: способ оплаты приходит извне
        ticket.status = TicketStatus.PAID
        self.notifier.send(ticket.passenger, "Билет оплачен")

    def refund(self, ticket_id: int) -> None:
        ticket = self._get(ticket_id)
        ticket.status = TicketStatus.RETURNED
        self.notifier.send(ticket.passenger, "Билет возвращён")

    def _get(self, ticket_id: int) -> Ticket:
        ticket = self.repository.get(ticket_id)
        if ticket is None:
            raise TicketNotFoundError(f"Билет #{ticket_id} не найден")
        return ticket
