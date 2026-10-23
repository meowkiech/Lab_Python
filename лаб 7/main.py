'''
Лабораторная работа №7. Вариант 10. Железнодорожные перевозки.
Система управления поездами и билетами.
Операции: поиск рейса, бронирование, покупка, возврат билета.
Реализовать несколько способов оплаты.

Работа состоит из двух этапов:
    Этап 1 (problem_version.py) - версия с намеренными нарушениями SOLID;
    Этап 2 (остальные файлы)    - рефакторинг по принципам SOLID.

Структура (этап 2):
    models.py        - сущности и перечисление (dataclass, Enum);
    interfaces.py    - интерфейсы (Protocol) и абстракция оплаты (ABC);
    repositories.py  - InMemoryTicketRepository (хранение билетов);
    payments.py      - способы оплаты (OCP);
    notifier.py      - уведомления;
    services.py      - бизнес-логика (DIP: зависимости извне);
    ui.py            - консольный интерфейс (input/print);
    main.py          - сборка зависимостей и запуск.
'''

from repositories import InMemoryTicketRepository
from notifier import ConsoleNotifier
from services import TicketService
from ui import ConsoleUI
from models import Train


def main() -> None:
    repository = InMemoryTicketRepository()        # LSP: можно заменить другой реализацией
    notifier = ConsoleNotifier()
    service = TicketService(repository, notifier)   # DIP: зависимости внедряются извне

    trains = [
        Train(1, "001А", "Москва - Санкт-Петербург", 20),
        Train(2, "055В", "Москва - Казань", 16),
        Train(3, "120С", "Санкт-Петербург - Казань", 12),
    ]

    ui = ConsoleUI(service, trains)
    ui.run()

if __name__ == "__main__":
    main()
