def Calculate(n,temp): # 종료 조건, 
    global max_result, min_result

    if n == N-1:
        if max_result < temp:
            max_result = temp
        if min_result > temp:
            min_result = temp
        return
    
    if Operators_arr[0] > 0:
        Operators_arr[0]-=1
        Calculate(n+1, temp+A_arr[n+1])
        Operators_arr[0]+=1

    if Operators_arr[1] > 0:
        Operators_arr[1]-=1
        Calculate(n+1, temp-A_arr[n+1])
        Operators_arr[1]+=1

    if Operators_arr[2] > 0:
        Operators_arr[2]-=1
        Calculate(n+1, temp*A_arr[n+1])
        Operators_arr[2]+=1

    if Operators_arr[3] > 0:
        Operators_arr[3]-= 1
        if temp < 0:
            result = -(abs(temp) // A_arr[n+1])
        else:
            result = temp//A_arr[n+1]
        Calculate(n+1, result)
        Operators_arr[3]+= 1
    

N=int(input()) # N은 2이상 11이하
A_arr=list(map(int,input().split())) # N개의 값 받음
Operators_arr=list(map(int,input().split())) # 덧셈, 뺄셈, 곱셈, 나눗셈 순서대로 N-1개 주어짐

max_result=-21e8
min_result=21e8

Calculate(0,A_arr[0])


print(max_result)
print(min_result)