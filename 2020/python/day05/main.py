import os


def find_seats(max):
    seats = [i for i in range(max)]
    while len(seats):
        dir = yield
        if dir == 'F' or dir == 'L':
            seats = seats[0:int(len(seats)/2)]
        elif dir == 'B' or dir == 'R':
            seats = seats[int(len(seats)/2):]

        yield seats


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        boarding_passes = f.read().splitlines()

    seat_ids = []
    for boarding_pass in boarding_passes:
        iter = find_seats(128)
        next(iter)
        for dir in boarding_pass[0:7]:
            rows_left = iter.send(dir)
            next(iter)

        iter = find_seats(8)
        next(iter)
        for dir in boarding_pass[7:]:
            cols_left = iter.send(dir)
            next(iter)

        seat_ids.append(rows_left[0] * 8 + cols_left[0])

    # Part 1
    print('Part 1 answer: ', max(seat_ids))

    # Part 2
    print('Part 2 answer: ', set(
        range(min(seat_ids), max(seat_ids) + 1)) - set(seat_ids))


if __name__ == '__main__':
    main()
