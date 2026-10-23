from models import Ticket, TicketStatus
from interfaces import PricingStrategy
from factories import TicketFactory


class TicketNotFoundError(Exception):
    pass


class TicketService:
    def __init__(self, repository) -> None:
        self.repository = repository      # Repository передаётся извне
        self._next_id = 1

    def create_ticket(self, passenger: str, train_number: str, car_type: str,
                      strategy: PricingStrategy) -> Ticket:
        ticket = TicketFactory.create(self._next_id, passenger, train_number, car_type)
        ticket.price = strategy.calculate(ticket.base_price)   # Strategy задаёт цену
        self._next_id += 1
        self.repository.add(ticket)
        return ticket

    def pay(self, ticket_id: int) -> None:
        ticket = self._get(ticket_id)
        ticket.status = TicketStatus.PAID

    def refund(self, ticket_id: int) -> None:
        ticket = self._get(ticket_id)
        ticket.status = TicketStatus.RETURNED

    def _get(self, ticket_id: int) -> Ticket:
        ticket = self.repository.get(ticket_id)
        if ticket is None:
            raise TicketNotFoundError(f"Билет #{ticket_id} не найден")
        return ticket
