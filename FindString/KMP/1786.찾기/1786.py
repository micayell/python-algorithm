T=input()
P=input()

def kmp_search(text,pattern):
    n,m=len(text),len(pattern)

    lps=[0]*m
    j=0
    for i in range(1,m):
        while j>0 and pattern[i] != pattern[j]:
            j=lps[j-1]
        if pattern[i] == pattern[j]:
            j+=1
            lps[i]=j

    results=[]
    j=0
    for i in range(n):
        while j>0 and text[i] != pattern[j]:
            j=lps[j-1]
        if text[i]==pattern[j]:
            if j==m-1:
                results.append(i-m+2)
                j=lps[j]

            else:
                j+=1

    return results

ans=kmp_search(T,P)
print(len(ans))
print(*(ans))