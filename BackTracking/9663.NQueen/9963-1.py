def check(current_row):
    for prev_row in range(current_row): # 이전 행에 대한 조사
        if row[current_row] == row[prev_row]:
            return False
        if abs(current_row-prev_row) == abs(row[current_row]-row[prev_row]):
            return False            
    return True

def n_queen(current_row):
    global cnt

    if current_row == n:
        cnt+=1
        return
    
    for i in range(n):
        row[current_row]=i # 퀸 위치 저장
        if check(current_row):
            n_queen(current_row+1)

n=int(input())

cnt=0
row=[0]*n
n_queen(0)
print(cnt)