import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
events = []
for _ in range(N):
    s, e = map(int, input().split())
    events.append((s, e + 1))  # e' = e + 1

# 종료(e')가 빠른 순 정렬 (동률이면 시작 빠른 순은 있어도 되고 없어도 됨)
events.sort(key=lambda x: (x[1], x[0]))

cnt = 0
last_end = -10**18  # 충분히 작은 값

for s, e_prime in events:
    if s >= last_end:
        cnt += 1
        last_end = e_prime

print(cnt)

'''
행사 종료 뒤 최소 1시간 뒤에 시작 가능 -> 종료 시간을 종료 + 1(e_prime)로 변경하기
정렬 기준을 끝나는 시간으로 잡는 거 기억하기.
'''