#!/usr/bin/env python

import sys

sys.path.append("/Users/shanglin/projects/google_code_jam")
from gcj_boilerplate import *

initialize()
T = read_int()

for t in range(1, T + 1):
    N = read_int()
    print(T)
    counter = dict()
    missing = []

    for n in range(2 * N - 1):
        row = read_int_list()
        for height in row:
            if height not in counter:
                counter[height] = 1
            else:
                counter[height] += 1
    for k, v in counter.items():
        if v % 2 != 0:
            missing.append(k)
    result = ' '.join([str(val) for val in sorted(missing)])
    print(result)
    output(t, result)

end()