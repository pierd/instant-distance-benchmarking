#!/usr/bin/env python3

import random
import timeit

import instant_distance

points = [[random.random() for _ in range(300)] for _ in range(1024)]
config = instant_distance.Config()

print(timeit.timeit('instant_distance.Hnsw.build(points, config)', number=10, globals=globals()))
