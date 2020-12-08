import os
import string


def split_list(input_list, separator):
    sub_list = []
    for item in input_list:
        if item == separator:
            yield sub_list
            sub_list = []
        else:
            sub_list.append(item)
    yield sub_list


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        lines = f.read().splitlines()

    # Parse input to list of unique yes answers: 'abcaa' -> 'abc'
    group_answers = [''.join(list(set(''.join(item)))) for item in split_list(lines, '')]

    questions = string.ascii_lowercase

    answers = {}
    for question in questions:
        answers[question] = ''.join(group_answers).count(question)

    # Part 1
    print('Part 1 answer: ', sum(answers.values()))

    # Part 2
    # Parse input to list of dictionaries
    group_answers = [{'num_members': len(item), 'answers': ''.join(item)} for item in split_list(lines, '')]

    for question in questions:
        answers[question] = 0
        for group_answer in group_answers:
            if group_answer['num_members'] == group_answer['answers'].count(question):
                answers[question] +=1
    
    print('Part 2 answer: ', sum(answers.values()))


if __name__ == '__main__':
    main()
