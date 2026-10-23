from models import Ticket

class InMemoryTicketRepository:
    def __init__(self) -> None:
        self._items: list[Ticket] = []

    def add(self, ticket: Ticket) -> None:
        self._items.append(ticket)

    def remove(self, ticket_id: int) -> None:
        self._items = [t for t in self._items if t.id != ticket_id]

    def get(self, ticket_id: int) -> Ticket | None:
        for t in self._items:
            if t.id == ticket_id:
                return t
        return None

    def get_all(self) -> list[Ticket]:
        return list(self._items)
