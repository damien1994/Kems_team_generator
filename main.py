import random

people = ['toto', 'gerard', 'max', 'leon']


def main(input):
    result = []
    while input:
        pairs = random.sample(input, 2)
        result.append(tuple(pairs))
        input = [name for name in input if name not in pairs]
    return result


if __name__ == '__main__':
    print(main(people))
