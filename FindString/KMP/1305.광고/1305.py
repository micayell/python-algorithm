# 광고판의 크기
# 광고판에 보이는 문자열

# 가능한 광고의 길이 중 가장 짧은 것의 길이

L=int(input())
S=input()

def solve(L,S):
    pi=[0]*L
    j=0

    for i in range(1,L):
        while j >0 and S[i] != S[j]:
            j=pi[j-1]

        if S[i] == S[j]:
            j+=1
            pi[i]=j

    print(L-pi[L-1])

solve(L,S)