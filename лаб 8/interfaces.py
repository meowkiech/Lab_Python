from typing import Protocol
from models import Ticket


# Repository: интерфейс доступа к данным
class Repository(Protocol):
    def add(self, ticket: Ticket) -> None:
        ...

    def get(self, ticket_id: int) -> Ticket | None:
        ...

    def get_all(self) -> list[Ticket]:
        ...

    def delete(self, ticket_id: int) -> None:
        ...


# Strategy: интерфейс алгоритма расчёта цены
class PricingStrategy(Protocol):
    def calculate(self, base_price: float) -> float:
        ...


# Command: интерфейс операции-объекта
class Command(Protocol):
    def execute(self) -> None:
        ...
