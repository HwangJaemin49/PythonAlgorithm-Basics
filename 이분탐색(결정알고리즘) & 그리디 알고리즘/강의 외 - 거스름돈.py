# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

import sys

def input():
	return sys.stdin.readline().rstrip('\n')

N = int(input())
cnt = 0

coins = [40, 20, 10, 5, 1]

for coin in coins:
	q, N = divmod(N, coin)
	cnt += q

print(cnt)

'''
그리디 알고리즘인지 잘 확인하기(각 동전이 이전 동전의 배수)
divmod라는 함수도 있다는 거 기억하기
'''