'''
기존 코드
아이디어 자체는 문제가 없었음. 다만 구현 과정에서 for 문 안에 prev를 넣어 prev가 계속 초기화 되고 있었음! 이거 주의하기
'''

N = int(input())
probs = list(map(int, input().split()))
scores = [0]*N

prev = 0
for i in range(N):
    if probs[i] == 1:
        prev += 1
        scores[i] = prev
    else:
        prev = 0
        scores[i] = 0

print(sum(scores))

'''
강의 풀이 버전
따로 점수 리스트를 만들지 않아 깔끔
'''
n = int(input())
a = list(map(int, input().split()))
sum = 0
cnt = 0
for x in a:
    if x == 1:
        cnt +=1 
        sum += cnt
    else:
        cnt =0
