import inspect
from models import Ticket, Train, TicketStatus, TicketNotFoundError, SeatTakenError
from protocols import Reportable
from decorators import log_call, measure_time, repeat


@log_call
def add_ticket(tickets: list[Ticket], ticket: Ticket) -> int:
    for t in tickets:
        same_seat = (t.train_number == ticket.train_number and
                     t.carriage_number == ticket.carriage_number and
                     t.seat == ticket.seat)
        if same_seat and t.status != TicketStatus.RETURNED:
            raise SeatTakenError(f"Место {ticket.seat} в вагоне {ticket.carriage_number} уже занято")
    tickets.append(ticket)
    return ticket.id


@log_call
def remove_ticket(tickets: list[Ticket], ticket_id: int) -> bool:
    ticket = find_ticket(tickets, ticket_id)
    tickets.remove(ticket)
    return True


def find_ticket(tickets: list[Ticket], ticket_id: int) -> Ticket:
    for t in tickets:
        if t.id == ticket_id:
            return t
    raise TicketNotFoundError(f"Билет #{ticket_id} не найден")


def find_train(trains: list[Train], number: str) -> Train | None:
    for tr in trains:
        if tr.number == number:
            return tr
    return None


def change_status(ticket: Ticket, new_status: TicketStatus) -> None:
    if ticket.status == TicketStatus.RETURNED:
        raise ValueError("Возвращённый билет нельзя изменить")
    ticket.status = new_status


@measure_time
def train_load(train: Train, tickets: list[Ticket]) -> float:
    busy = [t for t in tickets
            if t.train_number == train.number and t.status != TicketStatus.RETURNED]
    total = train.total_seats()
    if total == 0:
        raise ZeroDivisionError("У поезда нет вагонов с местами")
    return len(busy) / total * 100


def free_seats(train: Train, tickets: list[Ticket]) -> dict[int, list[int]]:
    result: dict[int, list[int]] = {}
    for c in train.carriages:
        taken = {t.seat for t in tickets
                 if t.train_number == train.number
                 and t.carriage_number == c.number
                 and t.status != TicketStatus.RETURNED}
        result[c.number] = [s for s in range(1, c.seats + 1) if s not in taken]
    return result


def get_statistics(tickets: list[Ticket]) -> dict:
    total = len(tickets)
    paid = len([t for t in tickets if t.status == TicketStatus.PAID])
    used = len([t for t in tickets if t.status == TicketStatus.USED])
    reserved = len([t for t in tickets if t.status == TicketStatus.RESERVED])
    returned = len([t for t in tickets if t.status == TicketStatus.RETURNED])
    prices = [t.price for t in tickets if t.status != TicketStatus.RETURNED]
    revenue = sum(prices)
    average = revenue / len(prices) if prices else 0
    return {
        "Всего билетов": total,
        "Забронировано": reserved,
        "Оплачено": paid,
        "Использовано": used,
        "Возвращено": returned,
        "Выручка": revenue,
        "Средняя цена": round(average, 2),
    }


@repeat(2)
def print_report(obj: Reportable) -> None:
    print("  >>", obj.get_report_data())


def inspect_object(obj) -> None:
    print("=== ИНФОРМАЦИЯ ОБ ОБЪЕКТЕ ===")
    print("Тип:", type(obj).__name__)
    print("Это билет?", isinstance(obj, Ticket))
    print("Атрибуты:")
    for name in dir(obj):
        if name.startswith("_"):
            continue
        value = getattr(obj, name)
        if not callable(value):
            print(f"    {name} = {value}")
    print("Методы:")
    for name in dir(obj):
        if name.startswith("_"):
            continue
        member = getattr(obj, name)
        if callable(member):
            print(f"    {name}{inspect.signature(member)}")
