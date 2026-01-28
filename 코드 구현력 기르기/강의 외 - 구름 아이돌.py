import sys

def input():
	return sys.stdin.readline().rstrip('\n')

N = int(input())

lst = list(map(int, input().split()))

pairs = [(lst[i], i+1) for i in range(N)]
pairs.sort(reverse=True)

for i in range(3):
	print(pairs[i][1], end= ' ')


'''
이중 리스트 구현 확실히 내 걸로 만들기!!
'''