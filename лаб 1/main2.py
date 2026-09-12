def sum_income(income):
    sum_ = 0
    for i in income.values():
        sum_ += i
    return sum_

def max_income(income):
    max_ = -1.0
    month = ''
    for key, val in income.items():
        if val > max_:
            max_ = max(val, max_)
            month = key
        elif val == max_:
            month += ', ' + key
    return month, max_

def min_income(income):
    min_ = 10.0 ** 7
    month = ''
    for key, val in income.items():
        if val < min_:
            min_ = min(val, min_)
            month = key
        elif val == min_:
            month += ', ' + key
    return month, min_

def average(income):
    return sum_income(income)/12

def more_than_average(income):
    list_ = []
    average_ = average(income)
    for i in income.values():
        if i > average_:
            list_.append(i)
    return len(list_)

def main():
    while True:
        print('==================',
              'Вариант 10: Доход предприятия',
              '1 - запуск',
              '0 - выход',
              '==================', sep='\n')
        menu = int(input())
        flag = False
        if menu == 0:
            break
        income = dict()
        month = ['Январь', 'Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']
        for i in range(12):
            while True:
                month_income = float(input(f"Доход за {month[i]} "))
                if month_income >= 0:
                    break
                else:
                    print('Доход не может быть меньше 0')
            income[month[i]] = month_income

        print('Годовой доход = ', sum_income(income))
        print('Среднемесячный доход = ', average(income))
        if max_income(income)[0].find(',') > 0:
            if max_income(income)[0].count(',') == 11:
                print('Доход одинаков за каждый месяц')
            else:
                print('Самые прибыльные месяцы:', max_income(income)[0], '(', max_income(income)[1], ')')
        else:
            print('Самый прибыльный месяц:', max_income(income)[0], '(', max_income(income)[1], ')')

        if min_income(income)[0].find(',') > 0:
            print('Наименее прибыльные месяцы:', min_income(income)[0], '(', min_income(income)[1], ')')
        else:
            print('Наименее прибыльный месяц:', min_income(income)[0], '(', min_income(income)[1], ')')
        print('Количество месяцев с прибылью больше среднего', more_than_average(income))

if __name__ == '__main__':
    main()

