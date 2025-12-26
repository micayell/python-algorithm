n=int(input())
text=input()

def rabin_carp(L,n,text):
    if L==0:
        return 1
    
    base=31
    mod=(1<<61)-1

    h_t=0
    h=base**(L-1)%mod

    for i in range(L):
        h_t = (h_t*base + (ord(text[i]) - ord('a') + 1))%mod

    seen = {h_t}

    for i in range(n-L):
        val_out = ord(text[i]) - ord('a') + 1
        val_in = ord(text[i+L]) - ord('a') + 1

        h_t = (base*(h_t-val_out*h)+val_in)%mod

        if h_t <0:
            h_t += mod

        if h_t in seen:
            return 1
        
        seen.add(h_t)

    return 0

low=0
high = n-1
ans=0

while low <= high:
    mid = (low+high)//2
    if rabin_carp(mid,n,text):
        ans = mid
        low = mid+1
    else:
        high = mid -1

print(ans)
