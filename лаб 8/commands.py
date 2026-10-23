from models import Ticket
from interfaces import PricingStrategy
from services import TicketService


# Command: каждая операция оформлена отдельным объектом с методом execute()
class BuyTicketCommand:
    def __init__(self, service: TicketService, passenger: str, train_number: str,
                 car_type: str, strategy: PricingStrategy) -> None:
        self.service = service
        self.passenger = passenger
        self.train_number = train_number
        self.car_type = car_type
        self.strategy = strategy
        self.ticket: Ticket | None = None

    def execute(self) -> None:
        self.ticket = self.service.create_ticket(
            self.passenger, self.train_number, self.car_type, self.strategy)
        self.service.pay(self.ticket.id)


class ReturnTicketCommand:
    def __init__(self, service: TicketService, ticket_id: int) -> None:
        self.service = service
        self.ticket_id = ticket_id

    def execute(self) -> None:
        self.service.refund(self.ticket_id)
