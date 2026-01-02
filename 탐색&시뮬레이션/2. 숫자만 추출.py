word = list(input())
nums = ''
cnt = 1

for ch in word:
    if ch.isalpha():
        continue
    else: nums += ch

nums = int(nums)
for i in range(2, nums+1):
    if nums % i == 0:
        cnt += 1
print(nums)
print(cnt)

'''isalpha() 기억하기'''