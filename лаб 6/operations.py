from models import *

def new_train(id_, route):
    train = []
    railcars = []
    seats = []

    train_ = Train(id_, route)
    for coupe in range(train_.coupe_num):
        railcars.append(Railcar(coupe + 1, RailType.COUPE, 36, id_))
    for platz in range(train_.platz_num):
        railcars.append(Railcar(platz + 1, RailType.PLATZCART, 54, id_))

    for rail in range(1, len(railcars) + 1):
        for seat_ in range(1, railcars[rail - 1].capacity + 1):
            if railcars[rail - 1].rail_type == RailType.COUPE:
                if seat_ % 2 == 0:
                    seats.append(Seat(seat_, SeatType.UP, railcars[rail - 1].id))
                else:
                    seats.append(Seat(seat_, SeatType.DOWN, railcars[rail - 1].id))
            else:
                if seat_ % 4 == 1:
                    seats.append(Seat(seat_, SeatType.UP, railcars[rail - 1].id))
                elif seat_ % 4 == 2:
                    seats.append(Seat(seat_, SeatType.DOWN, railcars[rail - 1].id))
                elif seat_ % 4 == 3:
                    seats.append(Seat(seat_, SeatType.SIDE_UP, railcars[rail - 1].id))
                elif seat_ % 4 == 0:
                    seats.append(Seat(seat_, SeatType.SIDE_DOWN, railcars[rail - 1].id))

    train.append(train_)
    train.append(railcars)
    train.append(seats)
    return train
