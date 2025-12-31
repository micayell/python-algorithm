# 문자열의 길이
# 영문 소문자로만 이루어진 문자열

# 해시값을 정수로 출력

L=int(input())
munza=input()

M=1234567891
r=31

res=0
for i in range(L):
    num = ord(munza[i])-96
    res+=(num*(r**i))

print(res%M)