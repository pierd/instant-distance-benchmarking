#!/usr/bin/env python3

import timeit
import statistics
import sys

import instant_distance

def load_points(path, count=100_000):
    words = []
    points = []
    with open(path, 'r') as input_file:
        input_file.readline()   # skip first line
        for _ in range(count):
            parts = input_file.readline().split(' ')
            words.append(parts[0])
            points.append([float(i) for i in parts[1:]])
    return words, points


if __name__ == '__main__':
    print(f'Loading words...')
    words, points = load_points('wiki.en.align.vec', count=100_000)

    print(f'Benchmarking...')

    config = instant_distance.Config()
    result = []
    timer = timeit.Timer(
        'instant_distance.HnswMap.build(points, words, config)',
        globals=globals(),
    )
    for _ in range(5):
        result.append(timer.timeit(1))
        print('.', end='')
        sys.stdout.flush()
    print()

    print(f'min: {min(result)} median: {statistics.median(result)} max: {max(result)} stdev: {statistics.stdev(result)}')
