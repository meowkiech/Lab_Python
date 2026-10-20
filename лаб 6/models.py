from dataclasses import dataclass, field
from enum import Enum


class TicketStatus(Enum):
    RESERVED = "забронирован"
    PAID = "оплачен"
    USED = "использован"
    RETURNED = "возвращён"


class TicketNotFoundError(Exception):
    pass


class SeatTakenError(Exception):
    pass


@dataclass
class Entity:
    id: int


@dataclass
class Carriage(Entity):
    number: int
    seats: int


@dataclass
class Train(Entity):
    number: str
    route: str
    carriages: list[Carriage] = field(default_factory=list)

    def total_seats(self) -> int:
        return sum(c.seats for c in self.carriages)

    def get_report_data(self) -> str:
        return f"Поезд №{self.number} ({self.route}), вагонов: {len(self.carriages)}, мест: {self.total_seats()}"


@dataclass
class Ticket(Entity):
    passenger: str
    train_number: str
    carriage_number: int
    seat: int
    price: float
    status: TicketStatus = TicketStatus.RESERVED

    def get_report_data(self) -> str:
        return f"Билет #{self.id}: {self.passenger}, поезд {self.train_number}, вагон {self.carriage_number}, место {self.seat} — {self.status.value}"
