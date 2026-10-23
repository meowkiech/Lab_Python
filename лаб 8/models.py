from dataclasses import dataclass
from enum import Enum


class TicketStatus(Enum):
    RESERVED = "забронирован"
    PAID = "оплачен"
    USED = "использован"
    RETURNED = "возвращён"


@dataclass
class Ticket:
    id: int
    passenger: str
    train_number: str
    car_type: str
    base_price: float
    price: float = 0.0
    status: TicketStatus = TicketStatus.RESERVED
