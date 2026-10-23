'''
Лабораторная работа №8. Вариант 10. Железнодорожные перевозки.
Система продажи билетов.

Паттерны:
    Repository - InMemoryTicketRepository (хранение билетов);
    Factory    - TicketFactory (создание билета по типу вагона: сидячий, купе, СВ);
    Strategy   - StandardPricing, DiscountPricing, DynamicPricing (расчёт цены);
    Command    - BuyTicketCommand, ReturnTicketCommand (операции-объекты + история).

Этапы:
    naive_version.py - этап 1, наивная реализация без паттернов;
    остальные файлы  - этап 3, рефакторинг с применением паттернов.
'''

from repositories import InMemoryTicketRepository
from services import TicketService, TicketNotFoundError
from strategies import StandardPricing, DiscountPricing, DynamicPricing
from commands import BuyTicketCommand, ReturnTicketCommand

STRATEGIES = {
    "1": StandardPricing(),
    "2": DiscountPricing(),
    "3": DynamicPricing(),
}
CAR_TYPES = {"1": "сидячий", "2": "купе", "3": "СВ"}


def main() -> None:
    repository = InMemoryTicketRepository()
    service = TicketService(repository)
    history = []            # история выполненных команд (Command)

    while True:
        print("===== ПРОДАЖА ЖЕЛЕЗНОДОРОЖНЫХ БИЛЕТОВ =====",
              "1 - Купить билет",
              "2 - Вернуть билет",
              "3 - Показать все билеты",
              "4 - История операций",
              "0 - Выход", sep="\n")
        choice = input("Выберите пункт меню: ")

        if choice == "1":
            try:
                passenger = input("ФИО пассажира: ")
                train_number = input("Номер поезда: ")
                print("Тип вагона: 1 - сидячий, 2 - купе, 3 - СВ")
                car_type = CAR_TYPES.get(input("Выберите: "))
                print("Тариф: 1 - стандартный, 2 - льготный, 3 - динамический")
                strategy = STRATEGIES.get(input("Выберите: "))
                if car_type is None or strategy is None:
                    print("Некорректный выбор.")
                    continue
                command = BuyTicketCommand(service, passenger, train_number, car_type, strategy)
                command.execute()
                history.append(f"Куплен билет #{command.ticket.id} за {command.ticket.price} руб.")
                print(f"Куплен билет #{command.ticket.id} за {command.ticket.price} руб.")
            except ValueError as e:
                print("Ошибка:", e)

        elif choice == "2":
            try:
                ticket_id = int(input("ID билета: "))
                command = ReturnTicketCommand(service, ticket_id)
                command.execute()
                history.append(f"Возвращён билет #{ticket_id}")
                print("Билет возвращён.")
            except TicketNotFoundError as e:
                print("Ошибка:", e)
            except ValueError:
                print("Ошибка: введено не число.")

        elif choice == "3":
            tickets = repository.get_all()
            if not tickets:
                print("Билетов нет.")
            for t in tickets:
                print(f"#{t.id}: {t.passenger}, поезд {t.train_number}, "
                      f"{t.car_type}, {t.price} руб. — {t.status.value}")

        elif choice == "4":
            if not history:
                print("Операций ещё не было.")
            for i, record in enumerate(history, 1):
                print(f"{i}. {record}")

        elif choice == "0":
            print("Программа завершена!")
            break
        else:
            print("Некорректный ввод.")


if __name__ == "__main__":
    main()
