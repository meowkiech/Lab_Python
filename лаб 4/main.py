'''
models.py
Содержит классы предметной области.

services.py
Содержит бизнес-логику.

storage.py
Отвечает за сохранение и загрузку данных.

exceptions.py
Содержит пользовательские исключения.

main.py
Отвечает за взаимодействие с пользователем и запуск программы.

Создать систему управления меню.
Хранить:
•	название блюда;
•	категорию;
•	цену;
•	калорийность.
Реализовать:
•	добавление;
•	удаление;
•	изменение цены;
•	поиск;
•	создание заказа;
•	сохранение меню и заказов.
Создать исключение при добавлении блюда с отрицательной ценой.
'''

import models
import storage
import exceptions
import services

#---чтение из джсон
dish_list_json = storage.read_dish_json()
dish_list_class = []
orders_list_class = []

#---создание списка объектов класса диш
try:
    for i in dish_list_json:
        dish = models.Dish(i[0], i[1], i[2], i[3])
        dish_list_class.append(dish)

    while True:
        print('Чё хочешь',
              '1 - добавить блюдо',
              '2 - удалить блюдо',
              '3 - изменить цену',
              '4 - поиск по имени и/или категории',
              '5 - создать заказ',
              '6 - выход', sep='\n')
        menu = input()
        if menu == '1':
            print("Добавление Блюда")
            dname = input("Введите название блюда ")
            dcategory = input("Введите категорию ")
            dprice = float(input("Введите цену "))
            dcaloric = input("Введите количество калорий ")

            newdish = models.Dish(dname, dcategory, dprice, dcaloric)
            dish_list_class.append(newdish)
            storage.write_dish_json(newdish)

        elif menu == '2':
            dname = input('Введите название блюда, которое хотите удалить: ')
            storage.delete_dish_by_name(dname)

        elif menu == '3':
            dname = input('Введите название блюда: ')
            dprice = float(input('Введите новую цену: '))
            storage.update_dish_price_by_name(dname, dprice)

        elif menu == '4':
            dname = input('Введите название блюда: ')
            print(storage.find_dishes(dname))

        elif menu == '5':

            while True:
                customer_name = input('Введите имя заказчика ')
                order = models.Order(services.new_order(dish_list_class), customer_name)
                order.price = services.final_price(order.names, dish_list_class)
                print(f'Ваш заказ: {order.names}',
                      f'Стоимость: {order.price}',
                      '1 - подтвердить, 2 - отказаться и повторить попытку, 3 - отказаться и вернутсья в меню', sep='\n')
                menu2 = input()
                if menu2 == '1':
                    order.order_done()
                    orders_list_class.append(order)
                    break
                elif menu2 == '2':
                    continue
                elif menu2 == '3':
                    break

        elif menu == '6':
            print('Завершение работы программы')
            break

        else:
            print('Некорректный ввод, повторите попытку')

except exceptions.FuckingLessZeroPrice:
    print('Цена блюда должна быть больше нуля!')

except ValueError:
    print("Некорректные данные, попробуйте ещё раз: ")