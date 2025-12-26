# 알파벳 소문자로만 이루어진게 포인트!

text=input()
pattern=input()

def rabin_karp(t,p):
    n=len(t)
    m=len(p)
    
    if n<m:
        return 0
    
    base = 31
    mod = 10**9+7

    h_t=0
    h_p=0
    h=1

    for i in range(m-1):
        h=(h*base)%mod
    
    for i in range(m):
        h_t=(h_t*base+(ord(t[i])-ord('a')+1))%mod
        h_p=(h_p*base+(ord(p[i])-ord('a')+1))%mod

    for i in range(n-m+1):
        if h_t == h_p:
            if t[i:i+m] == p:
                return 1
            
        if i < n-m:
            val_out = ord(t[i]) - ord('a') + 1
            val_in = ord(t[i+m]) - ord('a') + 1

            h_t = (base*(h_t-val_out*h)+val_in)%mod

            if h_t < 0:
                h_t += mod

    return 0

res=rabin_karp(text,pattern)
print(res)