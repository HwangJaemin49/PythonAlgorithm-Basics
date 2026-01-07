n = int(input())
listN = list(map(int, input().split()))
m = int(input())
listM = list(map(int, input().split()))

result = listN + listM
result.sort()
print(result)