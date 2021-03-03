import sys
import itertools
import time


def get_from_N(N):
    for i in range(1, N):
        yield i


def place_numbers(size, count):
    # получить позиции комбинации необходимой длины
    for positions in itertools.combinations(range(size), count):
        # перемешать позиции
        for i in itertools.permutations(range(len(positions))):
            p = [0] * size
            gen = get_from_N(size)
            for j in i:
                p[positions[j]] = next(gen)
            yield ''.join(str(x) for x in p)


if __name__ == '__main__':
    N = int(sys.argv[1])
    numbers = '0' * N + ''.join(str(x) for x in (range(1, N + 1)))
    start = time.time()
    result = list(place_numbers(len(numbers), N))
    print(time.time() - start)
    with open('output.txt', 'w') as f:
        f.write('\n'.join(line for line in result))
