N = int(input())
res = 0
for i in range(N):
    dices = input().split()
    dices.sort()
    a, b, c = map(int, dices)
    # 주사위 눈이 모두 같은 경우
    if a == b and b == c:
        money = 10000 + a*1000
    # 주사위 눈 중 두 개가 같은 경우
    elif a == b  or a == c:
        money = 1000 + a*100
    # 주사위 눈 중 두 개가 같은 경우
    elif b == c:
        money = 1000 + b*100
    else:
        money = c*100
    if money > res:
        res = money

print(res)