from abc import ABC, abstractmethod
from typing import Protocol
from models import Ticket


# ISP: два небольших специализированных интерфейса вместо одного большого
class TicketReader(Protocol):
    def get(self, ticket_id: int) -> Ticket | None:
        ...

    def get_all(self) -> list[Ticket]:
        ...

class TicketWriter(Protocol):
    def add(self, ticket: Ticket) -> None:
        ...

    def remove(self, ticket_id: int) -> None:
        ...

# Абстракция уведомлений
class Notifier(Protocol):
    def send(self, recipient: str, message: str) -> None:
        ...

# OCP: абстракция способа оплаты (новый способ = новый класс)
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        ...
