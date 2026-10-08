from models import VeggieDish

def final_price(names, data):
    price = 0
    for line in data:
        for name in names:
            if name == line.name:
                price += float(line.price)
    return price

def filter_by_caloric(data, max_calories):
    filtered_data = filter(lambda line: line.caloric <= max_calories, data)
    return list(filtered_data)

def get_all_prices(data):
    prices = map(lambda line: line.price, data)
    return list(prices)

def sort_by_price(data):
    return sorted(data, key=lambda line: line.price)

def get_average_caloric(data):
    try:
        all_calories = [line.caloric for line in data]
        average = sum(all_calories) / len(all_calories)
        return average
    except ZeroDivisionError:
        print("Ошибка: Список меню пуст, невозможно посчитать среднюю калорийность!")
        return 0

def has_veggie_dishes(data):
    check = any(isinstance(line, VeggieDish) for line in data)
    return check

def process_menu(data, action_function):
    return action_function(data)

def custom_filter(data, condition_function):
    results = []
    for line in data:
        if condition_function(line):
            results.append(line)
    return results