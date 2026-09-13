'''
Вариант 10. Доходы предприятия
Разработать программу анализа доходов предприятия по месяцам.
Пользователь вводит доход за каждый месяц.
Программа должна:
•	определить годовой доход;
•	определить среднемесячный доход;
•	найти наиболее прибыльный месяц;
•	найти наименее прибыльный месяц;
•	определить количество месяцев с доходом выше среднего.
'''

def sum_income(income):
    sum_ = 0
    for i in income.values():
        sum_ += i
    return sum_

def max_income(income):
    max_ = -1.0
    month = ''
    # --- каждую итерацию выбирается максимальное число и обновляется месяц
    # --- если числа равны то месяцы записываются, пока не будет найдено
    # --- более большое число или не завершится цикл
    for key, val in income.items():
        if val > max_:
            max_ = max(val, max_)
            month = key
        elif val == max_:
            month += ', ' + key
    return month, max_

def min_income(income):
    min_ = 10.0 ** 20
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
        menu = input()

        #---если доход одинаков за каждый месяц не должно быть более и менее прибыльного месяца
        equal_income = False

        if menu == '0':
            break
        elif menu == '1':
            income = dict()
            month = ['Январь', 'Февраль','Март','Апрель','Май','Июнь',
                     'Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']
            print('Доход за месяц не должен превышать 10^20')

            for i in range(12):
                while True:
                    month_income = (input(f"Доход за {month[i]} "))
                    try:
                        month_income = float(month_income)
                        if month_income >= 0 and month_income < 10 ** 20:
                            income[month[i]] = month_income
                            break
                        else:
                            print('Доход не может быть меньше 0 или больше 10^20')
                    except ValueError:
                        print('Некорректные данные, повторите попытку')



            print('Годовой доход = ', sum_income(income))
            print('Среднемесячный доход = ', average(income))

            # --- появляется разная надпись в зависимости от того
            # --- есть один или несколько самых прибыльных\неприбыльных
            # --- месяцев или их нет вообще

            if max_income(income)[0].find(',') > 0:
                if max_income(income)[0].count(',') == 11:
                    print('Доход одинаков за каждый месяц')
                    equal_income = True
                else:
                    print('Самые прибыльные месяцы:', max_income(income)[0],
                          '(', max_income(income)[1], ')')
            else:
                print('Самый прибыльный месяц:', max_income(income)[0],
                      '(', max_income(income)[1], ')')

            if min_income(income)[0].find(',') > 0 and not equal_income:
                print('Наименее прибыльные месяцы:', min_income(income)[0],
                      '(', min_income(income)[1], ')')
            else:
                if not equal_income:
                    print('Наименее прибыльный месяц:', min_income(income)[0],
                          '(', min_income(income)[1], ')')

            print('Количество месяцев с прибылью больше среднего', more_than_average(income))

        else:
            print('Неправильная команда, повторите попытку')

if __name__ == '__main__':
    main()

'''
⠀⠀⢀⣀⠤⠿⢤⢖⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡔⢩⠂⠀⠒⠗⠈⠀⠉⠢⠄⣀⠠⠤⠄⠒⢖⡒⢒⠂⠤⢄⠀⠀⠀⠀
⠇⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠈⠀⠈⠈⡨⢀⠡⡪⠢⡀⠀
⠈⠒⠀⠤⠤⣄⡆⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⠀⢕⠱⠀
⠀⠀⠀⠀⠀⠈⢳⣐⡐⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠁⠇
⠀⠀⠀⠀⠀⠀⠀⠑⢤⢁⠀⠆⠀⠀⠀⠀⠀⢀⢰⠀⠀⠀⡀⢄⡜⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⡦⠄⡷⠢⠤⠤⠤⠤⢬⢈⡇⢠⣈⣰⠎⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣃⢸⡇⠀⠀⠀⠀⠀⠈⢪⢀⣺⡅⢈⠆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠶⡿⠤⠚⠁⠀⠀⠀⢀⣠⡤⢺⣥⠟⢡⠃⠀
'''
