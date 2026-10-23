from models import Ticket


# Factory: создание билета нужного типа вагона сосредоточено в одном месте
class TicketFactory:
    PRICES = {
        "сидячий": 1000,
        "купе": 2500,
        "СВ": 5000,
    }

    @staticmethod
    def create(ticket_id: int, passenger: str, train_number: str, car_type: str) -> Ticket:
        if car_type not in TicketFactory.PRICES:
            raise ValueError(f"Неизвестный тип вагона: {car_type}")
        base_price = TicketFactory.PRICES[car_type]
        return Ticket(ticket_id, passenger, train_number, car_type, base_price)
