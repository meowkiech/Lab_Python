def final_price(names, data):
    price = 0
    for line in data:
        for name in names:
            if name == line.name:
                price += float(line.price)
    return price

def new_order(data):
    orders = []
    while True:
        order = input('Введите название позиции, или 0 если хотите закончить ')
        if order == '0':
            break
        else:
            for line in data:
                print(order, line, line.name)
                if order == line.name:
                    orders.append(order)
                    break
            else:
                print('Такой позиции нет в меню')

    return orders
