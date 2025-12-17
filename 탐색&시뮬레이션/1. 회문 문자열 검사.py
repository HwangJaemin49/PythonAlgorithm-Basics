N = int(input())

for i in range(N):
    word = input()
    word=word.upper()
    size = len(word)
    for j in range(size//2):
        if word[j] != word[-1-j]:
            print("NO")
            break
    else:
        print("YES")
    
'''
더 간단한 버전
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    if s == s[::-1]: # 기존 단어와 뒤집은 단어가 같을 때
        print("YES")
    else:
        print("NO")
'''