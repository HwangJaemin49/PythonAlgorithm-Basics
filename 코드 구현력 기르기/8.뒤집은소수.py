reverse_num = []
def reverse(x: str) -> int:
    return int(x[::-1])

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x%i == 0:
            return False
    else:
        return True

N = int(input())
nums = input().split()

for num in nums:
    tmp = reverse(num)
    if isPrime(tmp):
        print(tmp, end=' ')

