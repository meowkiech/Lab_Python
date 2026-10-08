import os
import json
import csv
from pydantic import BaseModel


class wDish(BaseModel):
    name: str
    category: str
    price: float
    caloric: float

def sync_to_json(dishes: list[wDish]):
    file_path = 'dish.json'
    # Дампим весь список моделей в валидный JSON-массив
    data = [dish.model_dump() for dish in dishes]
    with open(file_path, 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def append_to_csv(dish: wDish):
    file_path = 'dish.csv'
    file_exists = os.path.exists(file_path)

    with open(file_path, 'a', newline='', encoding="utf-8-sig") as f:
        writer = csv.writer(f, delimiter=';')
        # Если файл создается впервые, пишем заголовки
        if not file_exists:
            writer.writerow(['name', 'category', 'price', 'caloric'])
        writer.writerow([dish.name, dish.category, dish.price, dish.caloric])

def rewrite_csv(dishes: list[wDish]):
    file_path = 'dish.csv'
    with open(file_path, 'w', newline='', encoding="utf-8-sig") as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['name', 'category', 'price', 'caloric'])
        for dish in dishes:
            writer.writerow([dish.name, dish.category, dish.price, dish.caloric])

def load_from_json() -> list[wDish]:
    file_path = 'dish.json'
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r', encoding="utf-8") as f:
        try:
            data = json.load(f)
            return [wDish(**item) for item in data]
        except json.JSONDecodeError:
            return []


def write_dish_json(list_):
    dishes = load_from_json()

    # Проверка на дубликат имени
    for existing_dish in dishes:
        if existing_dish.name.lower() == list_.name.lower():
            print(f"Ошибка: Блюдо с именем '{list_.name}' уже существует в базе!")
            return

    dish = wDish(name=list_.name, category=list_.category, price=list_.price, caloric=list_.caloric)
    dishes.append(dish)
    sync_to_json(dishes)
    append_to_csv(dish)

    print(f"Блюдо '{list_.name}' успешно добавлено.")


def read_dish_json():
    dishes = load_from_json()
    list_ = []
    for dish in dishes:
        list_2 = []
        for i in dish:
            list_2.append(i[1])
        list_.append(list_2)
    return list_


def update_dish_price_by_name(target_name: str, new_price: float):
    dishes = load_from_json()
    updated = False

    for dish in dishes:
        if dish.name == target_name:
            dish.price = new_price
            updated = True

    if updated:
        sync_to_json(dishes)
        rewrite_csv(dishes)
        print(f"Блюдо '{target_name}' успешно обновлено.")
    else:
        print(f"Блюдо '{target_name}' не найдено.")


def delete_dish_by_name(target_name: str):
    dishes = load_from_json()
    initial_count = len(dishes)
    dishes = [dish for dish in dishes if dish.name != target_name]

    if len(dishes) < initial_count:
        sync_to_json(dishes)
        rewrite_csv(dishes)
        print(f"Блюдо '{target_name}' успешно удалено.")
    else:
        print(f"Блюдо '{target_name}' не найдено.")


def find_dishes(search_query):
    dishes = load_from_json()
    results = []
    for dish in dishes:
        if search_query.lower() in dish.name.lower():
            results.append(dish)
    return results