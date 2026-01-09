# 중복되지 않게

# 문서
# 문서의 길이 최대 2500
# 검색하고 싶은 단어가 주어짐
# 검색하고 싶은 단어는 최대 50

# 최대 몇 번 중복되지 않게 몇 번 등장하는지 구해야

text=input()
pattern=input()

def bruteforce_match(text,pattern):
    n=len(text)
    m=len(pattern)

    i=j=0
    cnt=0
    while j < m and i < n:
        if text[i] != pattern[j]:
            i=i-j
            j=-1
        i+=1
        j+=1

        if j==m:
            j=0
            cnt+=1
    
    return cnt
    
res = bruteforce_match(text,pattern)
print(res)