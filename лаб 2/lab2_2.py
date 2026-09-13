'''
Вариант 10. Рейсы
Для каждого рейса хранить:
•	номер;
•	направление;
•	продолжительность;
•	количество пассажиров.
Реализовать:
•	поиск рейсов по направлению;
•	фильтрацию по количеству пассажиров;
•	определение среднего количества пассажиров;
•	поиск самого продолжительного рейса;
•	список уникальных направлений;
•	сортировку по продолжительности.
'''
def load_trains(name_db):
    db = open(name_db)
    trains_db = db.readlines()
    trains = []
    train_data = ('id', 'from', 'to', 'time', 'pass_num')

    for i in trains_db:
        list_ = i.split('   ')
        tr = dict()
        for g in range(5):
            tr[train_data[g]] = list_[g].replace('\n','')
        trains.append(tr)
    return trains

def add_train(name_db):
    db = open(name_db, 'a')
    id = input('Введите номер рейса ')
    from_ = input('Введите направление рейса(откуда) ')
    to = input('Введите направление рейса(куда) ')
    time = input('Введите продолжительность ')
    pass_num = input('Введите количество пассажиров ')
    str_ = '\n' + id + '   ' + from_ + '   ' + to + '   ' + time + '   ' + pass_num
    db.write(str_)
    return {'id': id, 'from': from_, 'to': to, 'time': time,}

def declen(noun, num):
    # --- склонения существительных с чистительными
    num = str(num)
    if noun[-1] == 'а':
        if num[-1] == '1':
            return noun
        elif num[-1] in '234':
            return noun[:-1] + 'ы'
        else:
            return noun[:-1]
    else:
        if num[-1] == '1':
            return noun
        elif num[-1] in '234':
            return noun + 'а'
        else:
            return noun + 'ов'


def main():
    while True:
        trains = load_trains('trains_db.txt')
        print('==================',
              'Вариант 10. Рейсы',
              '1 - добавить рейс',
              '2 - отфильтровать рейсы',
              '3 - выход',
              '==================', sep='\n')
        menu = input('')

        if menu == '1':
            trains.append(add_train('trains_db.txt'))

        elif menu == '2':
            print('Выберите:',
                  '1 - поиск по направлению;',
                  '2 - поиск по количеству пассажиров',
                  '3 - самый продолжительный рейс',
                  '4 - список уникальных направлений',
                  '5 - сортировка по продолжительности',
                  '6 - среднее количество пассажиров',
                  '7 - возврат', sep='\n')
            menu2 = input('')

            if menu2 == '1':

                #отладочный принт, который в граф интерфейсе заменяется выпадающим списком
                print('Доступные варианты: ', *set([trains['from'] for trains in trains] +
                                               [trains['to'] for trains in trains]), sep='\n')
                menu3_1 = input('откуда: ')
                menu3_2 = input('куда: ')

                print(f"Номера рейсов по направлению '{menu3_1}' - '{menu3_2}':",
                      *[trains['id'] for trains in trains
                       if (menu3_1 in trains['from']) and (menu3_2 in trains['to'])],
                      sep='\n')

            elif menu2 == '2':
                while True:
                    menu3 = input('Введите количество пассажиров ')
                    try:
                        menu3 = int(menu3)
                        print(f"Номера рейсов вмещающих {menu3} {declen('пассажир',menu3)}: ",
                              [trains['id'] for trains in trains if trains['pass_num'] == str(menu3)])
                        break
                    except ValueError:
                        print('Неверное значение, повторите попытку')

            elif menu2 == '3':
                max_ = -1
                id_ = ['']
                for i in range(len(trains)):
                    if max_ < int(trains[i]['time']):
                        id_[0] = trains[i]['id']
                    elif max_ == int(trains[i]['time']):
                        id_.append((trains[i]['id']))
                    max_ = max(max_, int(trains[i]['time']))
                print(f"Рейсы {id_} идут в течении {max_} минут")

            elif menu2 == '4':
                uniq = [trains['from'] + ' - ' + trains['to'] for trains in trains ]
                set(uniq)
                print("Уникальные направления:", *uniq, sep='\n')
                continue

            elif menu2 == '5':
                while True:
                    print('Отсортировать по',
                          '1 - по возрастанию',
                          '2 - по убыванию', sep='\n')
                    menu3 = input()
                    sort_time = [int(trains['time'])for trains in trains]
                    sort_time.sort()
                    if menu3 == '2':
                        sort_time.reverse()

                    for i in sort_time:
                        print(f"Рейсы с продолжительностью {i} {declen('минута', i)} :",
                              [trains['id'] for trains in trains if trains['time'] == str(i)], sep='\n')
                    break

            elif menu2 == '6':
                average_ = sum([int(trains['pass_num']) for trains in trains])/len(trains)
                print(f"Среднее вместимое количество пассажиров всех рейсов: {average_}")

            #---чем дальше в лес if else if else
            elif menu2 == '7':
                continue

        elif menu == '3':
            break
        else:
            print('Неверная команда, повторите попытку')

if __name__ == '__main__':
    main()
