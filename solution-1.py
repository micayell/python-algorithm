T = int(input())
for _ in range(T):
    S = list(input())

    stack = ["("]
    if S[0] == "(" and S[-1] == ")" and len(S) % 2 == 0:
        idx = 0
        for idx in range(1, len(S)):
            if S[idx] == "(":
                stack.append("(")
            else:
                if stack:
                    stack.pop()
                else:
                    print("NO")
                    break
    elif stack:
        print("NO")
    else:
        print("YES")

