import os
import math


def calculate_next_departing_time(time, bus_number):
    return int(time / bus_number) * bus_number + bus_number


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        notes = f.read().splitlines()

    # Part 1
    departure_time = int(notes[0])
    buses = [int(entry) for entry in notes[1].split(',') if entry != 'x']

    min_time = None
    bus_to_catch = None
    for bus in buses:
        bus_departure_time = calculate_next_departing_time(departure_time, bus)

        if not min_time or min_time > bus_departure_time:
            min_time = bus_departure_time
            bus_to_catch = bus

    print('Part 1 answer: ', (bus_departure_time -
                              departure_time) * bus_to_catch)

    # Part 2
    buses = [int(entry) if entry !=
             'x' else None for entry in notes[1].split(',')]

    bus_intervals = []
    for i, bus in enumerate(buses):
        if bus:
            bus_intervals.append((bus, i))

    subsequent_times = []
    time = 100000000000000
    while len(subsequent_times) < len(bus_intervals):
        for i, bus_interval in enumerate(bus_intervals):
            bus_number, interval = bus_interval
            subsequent_times.append(
                calculate_next_departing_time(time + interval, bus_number))

            if i > 0 and subsequent_times[i] - subsequent_times[i-1] != bus_intervals[i][1] - bus_intervals[i-1][1]:
                step = 1
                for bus, bus_interval in bus_intervals[:i]:
                    step = step * bus
                time += step

                subsequent_times = []
                break

    print('Part 2 answer: ', min(subsequent_times))


if __name__ == '__main__':
    main()
