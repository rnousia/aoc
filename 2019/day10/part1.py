import os

def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        input = f.read().split('\n')

    print(input)

  
if __name__== '__main__':
  main()