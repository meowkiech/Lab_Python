'''
Вариант 10. Ресторан
Хранить:
•	название блюда;
•	категорию;
•	цену;
•	калорийность.
Реализовать:
•	фильтрацию блюд по калорийности;
•	получение списка цен;
•	сортировку по цене;
•	вычисление средней калорийности;
•	проверку наличия вегетарианских блюд;
•	генератор блюд выбранной категории.

1.	не менее одного базового класса;
2.	не менее двух производных классов;
3.	коллекцию объектов;
4.	функции обработки объектов;
5.	минимум две функции высшего порядка;
6.	минимум две lambda-функции;
7.	минимум один map();
8.	минимум один filter();
9.	минимум один вызов sorted(..., key=...);
10.	минимум один comprehension;
11.	минимум один генератор;
12.	минимум одну проверку с any() или all();
13.	собственный итератор или генератор;
14.	обработку исключительных ситуаций.

'''
from models import MeatDish, VeggieDish
from operations import (
    final_price,
    sort_by_price,
    filter_by_caloric,
    get_all_prices,
    get_average_caloric,
    has_veggie_dishes,
    process_menu
)
from generators import dish_generator_by_category

menu = [
    MeatDish("Борщ с говядиной", "Супы", 250, 350),
    VeggieDish("Салат Цезарь Вег", "Салаты", 180, 150),
    MeatDish("Стейк", "Горячее", 600, 500),
    VeggieDish("Овощи гриль", "Горячее", 220, 120)
]

# Точка входа для запуска тестов
def show_menu():
    while True:
        print("===== МЕНЮ =====",
              "1 - Показать все объекты",
              "2 - Отфильтровать объекты",
              "3 - Преобразовать данные",
              "4 - Отсортировать объекты",
              "5 - Выполнить статистический анализ",
              "6 - Запустить генератор",
              "7 - Проверить условие",
              "0 - Выход", sep="\n")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            print("\n--- Список всех блюд в меню ---")
            for item in menu:
                print(
                    f"Название: {item.name} | Категория: {item.category} | Цена: {item.price} руб. | Калорийность: {item.caloric} ккал")

        elif choice == "2":
            print("\n--- Фильтрация объектов по калорийности ---")
            try:
                max_cal = float(input("Введите максимальную калорийность: "))
                filtered_dishes = filter_by_caloric(menu, max_cal)
                if filtered_dishes:
                    for item in filtered_dishes:
                        print(f" Подходит: {item.name} ({item.caloric} ккал)")
                else:
                    print("Блюд с такой или меньшей калорийностью не найдено.")
            except ValueError:
                print("Ошибка: Введено не число!")

        elif choice == "3":
            print("\n--- Преобразование данных (Получение списка всех цен) ---")
            prices_list = get_all_prices(menu)
            print(f"Список цен всех позиций: {prices_list}")

        elif choice == "4":
            print("\n--- Сортировка объектов по цене ---")
            sorted_menu = sort_by_price(menu)
            for item in sorted_menu:
                print(f"{item.name} — {item.price} руб.")

        elif choice == "5":
            print("\n--- Статистический анализ (Средняя калорийность) ---")
            avg_caloric = get_average_caloric(menu)
            print(f"Средняя калорийность всех блюд в меню: {avg_caloric:.2f} ккал")

        elif choice == "6":
            print("\n--- Запуск генератора по категории ---")
            cat = input("Введите интересующую категорию (например: Горячее, Супы, Салаты): ")
            my_gen = dish_generator_by_category(menu, cat)

            print(f"Результаты генератора для категории '{cat}':")
            found = False
            for item in my_gen:
                print(f" Найдено через yield: {item.name}")
                found = True
            if not found:
                print("В этой категории пока нет блюд.")

        elif choice == "7":
            print("\n--- Проверка условия (Наличие вегетарианских блюд) ---")
            if has_veggie_dishes(menu):
                print(" Результат проверки: Да, в меню присутствуют вегетарианские блюда.")
            else:
                print(" Результат проверки: Нет, вегетарианских блюд в меню не обнаружено.")

        elif choice == "0":
            print("\nПрограмма завершена. Всего доброго!")
            break
        else:
            print("\nНекорректный ввод. Пожалуйста, выберите число от 0 до 7.")


if __name__ == "__main__":
    show_menu()
