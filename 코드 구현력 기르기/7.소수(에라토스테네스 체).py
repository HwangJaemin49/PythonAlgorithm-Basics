'''

처음 짠 코드
시간 복잡도 고려 못 함

N = int(input())
list = []

for i in range(2, N+1):
    total = 0
    for j in range(1, i+1):
        if i%j == 0:
            total += 1
    if(total == 2):
        list.append(i)

print(len(list))

'''

n = int(input())
ch = [0]*(n+1)
cnt = 0
for i in range(2, n+1):
    if ch[i]==0:
        cnt += 1
        for j in range(1, n+1, i):
            ch[j]=1
print(cnt)