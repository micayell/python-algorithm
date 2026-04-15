n = int(input())


def Euler_Phi(N):
    ans = N
    p = 2

    while p * p <= N:
        if N % p == 0:
            ans = ans - (ans // p)

            while N % p == 0:
                N = N // p
        p = p + 1

    if N > 1:
        ans = ans - (ans // N)

    return ans


answer = Euler_Phi(n)
print(answer)
