nums = [i for i in range(1, 21)]

for _ in range(10):
    a, b = map(int, input().split())
    nums[a-1:b] = reversed(nums[a-1:b])

for num in nums:
    print(num, end = ' ')

'''
nums[a:b+1] : a부터 b까지 (b 포함) 구간 슬라이스

reversed(…) : 그 구간을 뒤집은 이터레이터

nums[a:b+1] = … : 그 구간에 다시 집어넣기
'''