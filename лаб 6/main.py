'''
Лабораторная работа №6. Вариант 10. Железнодорожные перевозки.
Разработать систему управления поездами и билетами.
Объекты: поезд, вагон, билет.
Статусы билета: забронирован, оплачен, использован, возвращён.
Дополнительные операции:
    - расчёт загрузки поезда;
    - поиск свободных мест.

Минимальный набор операций:
1. Добавить объект
2. Удалить объект
3. Найти объект
4. Вывести все объекты
5. Изменить состояние объекта
6. Выполнить операцию предметной области
7. Получить статистику
8. Выполнить интроспекцию объекта
9. Демонстрация декораторов
10. Демонстрация контекстного менеджера
0. Выход

'''

import models
import services
from models import Train, Carriage, Ticket, TicketStatus
from context import Operation
from decorators import log_call, repeat

trains: list[Train] = [
    Train(1, "001А", "Москва - Санкт-Петербург",
          [Carriage(1, 1, 10), Carriage(2, 2, 10)]),
    Train(2, "055В", "Москва - Казань",
          [Carriage(3, 1, 8)]),
]

tickets: list[Ticket] = [
    Ticket(1, "Иванов И.И.", "001А", 1, 5, 2500, TicketStatus.PAID),
    Ticket(2, "Петров П.П.", "001А", 1, 6, 2500, TicketStatus.RESERVED),
    Ticket(3, "Сидоров С.С.", "055В", 3, 2, 1800, TicketStatus.USED),
]

next_id = 4


def demo() -> None:
    print("\n--- Демонстрация возможностей ---")
    print("dataclass:", tickets[0])
    print("Enum:", TicketStatus.PAID, "=", TicketStatus.PAID.value)
    train = trains[0]
    print("Protocol (get_report_data):")
    services.print_report(train)
    services.print_report(tickets[0])
    services.inspect_object(tickets[0])
    print("--- Конец демонстрации ---\n")


def main() -> None:
    global next_id
    demo()
    while True:
        print("===== МЕНЮ =====",
              "1 - Добавить билет",
              "2 - Удалить билет",
              "3 - Найти билет",
              "4 - Вывести все билеты",
              "5 - Изменить статус билета",
              "6 - Расчёт загрузки поезда / свободные места",
              "7 - Статистика",
              "8 - Интроспекция билета",
              "9 - Демонстрация декораторов",
              "10 - Демонстрация контекстного менеджера",
              "0 - Выход", sep="\n")
        choice = input("Выберите пункт меню: ")

        if choice == "1":
            try:
                passenger = input("ФИО пассажира: ")
                train_number = input("Номер поезда: ")
                carriage_number = int(input("Номер вагона: "))
                seat = int(input("Место: "))
                price = float(input("Цена: "))
                ticket = Ticket(next_id, passenger, train_number, carriage_number, seat, price)
                with Operation("добавление билета"):
                    services.add_ticket(tickets, ticket)
                next_id += 1
                print("Билет добавлен.")
            except models.SeatTakenError as e:
                print("Ошибка:", e)
            except ValueError:
                print("Ошибка: введено не число.")

        elif choice == "2":
            try:
                ticket_id = int(input("ID билета: "))
                services.remove_ticket(tickets, ticket_id)
                print("Билет удалён.")
            except models.TicketNotFoundError as e:
                print("Ошибка:", e)
            except ValueError:
                print("Ошибка: введено не число.")

        elif choice == "3":
            try:
                ticket_id = int(input("ID билета: "))
                print(services.find_ticket(tickets, ticket_id).get_report_data())
            except models.TicketNotFoundError as e:
                print("Ошибка:", e)
            except ValueError:
                print("Ошибка: введено не число.")

        elif choice == "4":
            for t in tickets:
                print(t.get_report_data())

        elif choice == "5":
            try:
                ticket_id = int(input("ID билета: "))
                ticket = services.find_ticket(tickets, ticket_id)
                print("Статусы:", ", ".join(s.name for s in TicketStatus))
                name = input("Новый статус: ").upper()
                services.change_status(ticket, TicketStatus[name])
                print("Статус изменён.")
            except models.TicketNotFoundError as e:
                print("Ошибка:", e)
            except KeyError:
                print("Ошибка: нет такого статуса.")
            except ValueError as e:
                print("Ошибка:", e)

        elif choice == "6":
            number = input("Номер поезда: ")
            train = services.find_train(trains, number)
            if train is None:
                print("Поезд не найден.")
            else:
                try:
                    load = services.train_load(train, tickets)
                    print(f"Загрузка поезда: {load:.1f}%")
                    print("Свободные места по вагонам:")
                    for carriage, seats in services.free_seats(train, tickets).items():
                        print(f"  Вагон {carriage}: {seats}")
                except ZeroDivisionError as e:
                    print("Ошибка:", e)

        elif choice == "7":
            for key, value in services.get_statistics(tickets).items():
                print(f"{key}: {value}")

        elif choice == "8":
            try:
                ticket_id = int(input("ID билета: "))
                services.inspect_object(services.find_ticket(tickets, ticket_id))
            except models.TicketNotFoundError as e:
                print("Ошибка:", e)
            except ValueError:
                print("Ошибка: введено не число.")

        elif choice == "9":
            @log_call
            def sample_sum(a: int, b: int) -> int:
                return a + b

            @repeat(3)
            def hello() -> None:
                print("Привет из декоратора repeat(3)")

            sample_sum(2, 3)
            hello()

        elif choice == "10":
            with Operation("демонстрация контекстного менеджера"):
                print("Выполняется работа внутри блока with...")

        elif choice == "0":
            print("Программа завершена!")
            break
        else:
            print("Некорректный ввод.")


if __name__ == "__main__":
    main()
