from dataclasses import dataclass
from enum import Enum

class TicketStatus(Enum):
    RESERVED = "забронирован"
    PAID = "оплачен"
    USED = "использован"
    RETURNED = "возвращён"

@dataclass
class Entity:
    id: int

@dataclass
class Train(Entity):
    number: str
    route: str
    seats: int

@dataclass
class Ticket(Entity):
    passenger: str
    train_number: str
    seat: int
    price: float
    status: TicketStatus = TicketStatus.RESERVED