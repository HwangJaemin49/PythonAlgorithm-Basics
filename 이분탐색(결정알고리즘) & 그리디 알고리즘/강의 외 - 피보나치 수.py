# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
def input():
	return sys.stdin.readline().rstrip('\n')

MOD = 1000000007

K = int(input())

if K == 1:
    print(0)
elif K == 2:
    print(1)
else:
    a, b = 0, 1
    for _ in range(3, K + 1):
        a, b = b, (a + b) % MOD
    print(b)

'''
피보나치 수 구현은 그냥 외우기
a, b = b, (a+b) 부분
함수로 만들면 깊이 때문에 런타임 에러가 나고, for 문으로 구하는 편이 좋음.
'''