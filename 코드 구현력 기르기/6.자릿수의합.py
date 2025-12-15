N = int(input())
nums = list(map(int, input().split()))
max = 0

def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x%10
        x = x//10
    return sum

for num in nums:
    total = digit_sum(num)
    if (total > max):
        max = total
        res = num
print(res)