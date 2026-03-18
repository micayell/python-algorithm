def dfs(depth):
    # 종료 조건: 모든 빈칸을 다 채웠을 때
    if depth == len(zeros): 
        # 스도쿠 보드 출력
        # 프로그램 완전 종료 (sys.exit(0))
        
    r, c = zeros[depth]
    
    for num in range(1, 10): # 1부터 9까지 작은 수부터 대입
        if 유효성_검사_통과(r, c, num):
            board[r][c] = num # 1. 숫자를 채워보고
            dfs(depth + 1)    # 2. 다음 빈칸을 향해 깊이 들어감
            board[r][c] = 0   # 3. ★핵심★ 실패하고 돌아왔다면 다시 0으로 원상복구 (백트래킹)