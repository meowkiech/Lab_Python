from pydantic import BaseModel
import os

class wDish(BaseModel):
    name: str
    category: str
    price: float
    caloric: float

def write_dish_json(list_):
    file_path = 'dish.jsonl'
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    existing_dish = wDish.model_validate_json(line)
                    if existing_dish.name.lower() == list_.name.lower():
                        print(f"Ошибка: Блюдо с именем '{list_.name}' уже существует в базе!")
                        return
    dish = wDish(name=list_.name, category=list_.category, price=list_.price, caloric=list_.caloric)

    with open(file_path, 'a', encoding="utf-8") as f:
        f.write(dish.model_dump_json() + '\n')
    print(f"Блюдо '{list_.name}' успешно добавлено.")

def read_dish_json():
    list_ = []
    with open('dish.jsonl', 'r', encoding="utf-8") as f:
        for line in f:
            if line.strip():
                list_2 = []
                str_ = wDish.model_validate_json(line)
                for i in str_:
                    list_2.append(i[1])
                list_.append(list_2)
    return list_

def update_dish_price_by_name(target_name: str, new_price: float):
    dishes = []
    updated = False

    with open('dish.jsonl', 'r', encoding="utf-8") as f:
        for line in f:
            if line.strip():
                dish = wDish.model_validate_json(line)
                if dish.name == target_name:
                    dish.price = new_price
                    updated = True
                dishes.append(dish)

    if updated:
        with open('dish.jsonl', 'w', encoding="utf-8") as f:
            for dish in dishes:
                f.write(dish.model_dump_json() + '\n')
        print(f"Блюдо '{target_name}' успешно обновлено.")
    else:
        print(f"Блюдо '{target_name}' не найдено.")


def delete_dish_by_name(target_name: str):
    dishes = []
    deleted = False

    with open('dish.jsonl', 'r', encoding="utf-8") as f:
        for line in f:
            if line.strip():
                dish = wDish.model_validate_json(line)
                if dish.name == target_name:
                    deleted = True
                    continue
                dishes.append(dish)

    if deleted:
        with open('dish.jsonl', 'w', encoding="utf-8") as f:
            for dish in dishes:
                f.write(dish.model_dump_json() + '\n')
        print(f"Блюдо '{target_name}' успешно удалено.")
    else:
        print(f"Блюдо '{target_name}' не найдено.")


def find_dishes(search_query):
    results = []

    with open('dish.jsonl', 'r', encoding="utf-8") as f:
        for line in f:
            if line.strip():
                dish = wDish.model_validate_json(line)
                if search_query.lower() in dish.name.lower():
                    results.append(dish)

    return results