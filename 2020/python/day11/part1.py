import os


def fill_seats(seat_map):
    filled_seats = [[c for c in row] for row in seat_map]
    for i, seat_row in enumerate(seat_map):
        for j, seat in enumerate(seat_row):
            if is_seat(seat):
                adjacent_seats = get_adjacent_seats((i, j), seat_map)
                if is_vacant_seat(seat) and count_occupied_seats(adjacent_seats) == 0:
                    filled_seats[i][j] = '#'
                elif not is_vacant_seat(seat) and count_occupied_seats(adjacent_seats) > 4:
                    filled_seats[i][j] = 'L'

    return [''.join(seats) for seats in filled_seats]


def is_seat(seat):
    return True if seat in ('L', '#') else False


def get_adjacent_seats(current_seat_index, seat_map):
    row, col = current_seat_index
    up = max(0, row-1)
    down = min(row+2, len(seat_map))

    left = max(0, col-1)
    right = min(col+2, len(seat_map[0]))

    return [seat_row[left:right] for seat_row in seat_map[up:down]]


def is_vacant_seat(seat):
    return True if seat == 'L' else False


def count_occupied_seats(seat_map):
    return [seat for seat_row in seat_map for seat in seat_row].count('#')


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        seat_map = f.read().splitlines()

    current_seat_map = seat_map.copy()
    previous_seat_map = []
    count = 0

    while ''.join(current_seat_map) != ''.join(previous_seat_map):
        previous_seat_map = current_seat_map.copy()
        current_seat_map = fill_seats(previous_seat_map)
        count += 1

    print('Part 1 answer: ', count_occupied_seats(current_seat_map))


if __name__ == '__main__':
    main()
