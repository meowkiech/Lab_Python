'''
Этап 1. Наивная реализация (без паттернов).

Проблемы:
- создание билета по типу вагона реализовано через if/elif (нужна Factory);
- расчёт цены по тарифу реализован через if/elif (нужна Strategy);
- операции (купить/вернуть) смешаны в одном методе через if/elif (нужен Command);
- данные хранятся в обычном списке внутри класса (нужен Repository).
При добавлении нового типа вагона, тарифа или операции приходится
изменять существующий метод process().
'''


class TicketApp:
    def __init__(self):
        self.tickets = []
        self.next_id = 1

    def process(self, command, passenger=None, train=None, car_type=None,
                tariff=None, ticket_id=None):
        if command == "buy":
            if car_type == "сидячий":
                base = 1000
            elif car_type == "купе":
                base = 2500
            elif car_type == "СВ":
                base = 5000
            else:
                print("Неизвестный тип вагона")
                return

            if tariff == "стандартный":
                price = base
            elif tariff == "льготный":
                price = base * 0.5
            elif tariff == "динамический":
                price = base * 1.3
            else:
                print("Неизвестный тариф")
                return

            ticket = {"id": self.next_id, "passenger": passenger,
                      "car": car_type, "price": price, "status": "оплачен"}
            self.tickets.append(ticket)
            self.next_id += 1
            print(f"Куплен билет #{ticket['id']} за {price} руб.")

        elif command == "return":
            for t in self.tickets:
                if t["id"] == ticket_id:
                    t["status"] = "возвращён"
                    print(f"Билет #{ticket_id} возвращён")
                    return
            print("Билет не найден")

        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    app = TicketApp()
    app.process("buy", passenger="Иванов И.И.", car_type="купе", tariff="стандартный")
    app.process("buy", passenger="Петров П.П.", car_type="СВ", tariff="льготный")
    app.process("return", ticket_id=1)
