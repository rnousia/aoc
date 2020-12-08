import os

def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        lines = f.read().splitlines()
    
    expenses = [int(line) for line in lines]
    result = None
    for i, item1 in enumerate(expenses):
        for j, item2 in enumerate(expenses):
                if i != j and item1 + item2 == 2020:
                    result = item1 * item2
                    return

    print('Part 1 answer: ', result)


if __name__== '__main__':
  main()
