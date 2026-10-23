from services import TicketService, TicketNotFoundError
from models import Train
from payments import CardPayment, CashPayment, BankTransfer


class ConsoleUI:
    def __init__(self, service: TicketService, trains: list[Train]) -> None:
        self.service = service
        self.trains = trains

    def run(self) -> None:
        while True:
            print("===== ЖЕЛЕЗНОДОРОЖНЫЕ ПЕРЕВОЗКИ =====",
                  "1 - Поиск поезда",
                  "2 - Забронировать билет",
                  "3 - Купить (оплатить) билет",
                  "4 - Вернуть билет",
                  "5 - Показать все билеты",
                  "0 - Выход", sep="\n")
            choice = input("Выберите пункт меню: ")
            if choice == "1":
                self._search()
            elif choice == "2":
                self._book()
            elif choice == "3":
                self._buy()
            elif choice == "4":
                self._refund()
            elif choice == "5":
                self._show_all()
            elif choice == "0":
                print("Программа завершена!")
                break
            else:
                print("Некорректный ввод.")

    def _find_train(self, number: str) -> Train | None:
        for t in self.trains:
            if t.number == number:
                return t
        return None

    def _search(self) -> None:
        route = input("Введите направление: ")
        found = self.service.search_trains(self.trains, route)
        if found:
            for t in found:
                print(f"Поезд №{t.number}: {t.route}, мест: {t.seats}")
        else:
            print("Поезда не найдены.")

    def _book(self) -> None:
        try:
            train = self._find_train(input("Номер поезда: "))
            if train is None:
                print("Поезд не найден.")
                return
            passenger = input("ФИО пассажира: ")
            seat = int(input("Место: "))
            price = float(input("Цена: "))
            ticket = self.service.book(train, passenger, seat, price)
            print(f"Забронирован билет #{ticket.id}")
        except ValueError:
            print("Ошибка: введено не число.")

    def _buy(self) -> None:
        methods = {"1": CardPayment(), "2": CashPayment(), "3": BankTransfer()}
        try:
            ticket_id = int(input("ID билета: "))
            print("Способ оплаты: 1 - картой, 2 - наличными, 3 - перевод")
            payment = methods.get(input("Выберите: "))
            if payment is None:
                print("Неизвестный способ оплаты.")
                return
            self.service.buy(ticket_id, payment)
            print("Билет оплачен.")
        except TicketNotFoundError as e:
            print("Ошибка:", e)
        except ValueError:
            print("Ошибка: введено не число.")

    def _refund(self) -> None:
        try:
            ticket_id = int(input("ID билета: "))
            self.service.refund(ticket_id)
            print("Билет возвращён.")
        except TicketNotFoundError as e:
            print("Ошибка:", e)
        except ValueError:
            print("Ошибка: введено не число.")

    def _show_all(self) -> None:
        tickets = self.service.repository.get_all()
        if not tickets:
            print("Билетов нет.")
        for t in tickets:
            print(f"#{t.id}: {t.passenger}, поезд {t.train_number}, место {t.seat} — {t.status.value}")
