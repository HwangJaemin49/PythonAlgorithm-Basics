# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys


def input():
    return sys.stdin.readline().rstrip('\n')


N, M = map(int, input().split())

seen = bytearray(N + 1)
remain = N

for idx in range(1, M + 1):
    x = int(input())
    if 1 <= x <= N and not seen[x]:
        seen[x] = 1
        remain -= 1
        if remain == 0:
            print(idx)
            sys.exit(0)

print(-1)


