class NumberGame():
    def __init__(self, starting_numbers):
        self.numbers = {}
        for i, number in enumerate(starting_numbers):
            self.numbers[number] = NumberToPlay(number, i)
        self.current_number_value = starting_numbers[-1]
        
    def play_next_number(self, index):
        value = self.numbers[self.current_number_value].current_index - \
            self.numbers[self.current_number_value].last_index
        if value not in self.numbers:
            self.numbers[value] = NumberToPlay(value, index)
        else:
            self.numbers[value].update(index)
        self.current_number_value = value

class NumberToPlay():
    def __init__(self, number, index):
        self.value = number
        self.current_index = index
        self.last_index = index

    def update(self, new_index):
        self.last_index = self.current_index
        self.current_index = new_index

    def __str__(self):
        return 'Value: {0}, current index:{2}'.format(self.value, self.current_index)


def main():
    # input
    starting_numbers = [16, 1, 0, 18, 12, 14, 19]
    # test input
    # starting_numbers = [0, 3, 6]

    game = NumberGame(starting_numbers)

    for i in range(len(starting_numbers), 30000000):
        game.play_next_number(i)

    print('Part 2 answer: ', game.current_number_value)


if __name__ == '__main__':
    main()
