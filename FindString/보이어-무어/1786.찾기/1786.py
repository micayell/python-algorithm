def horspool(text, pattern):
    n, m = len(text), len(pattern)
    if m > n: return []
    
    # 나쁜 문자 테이블을 배열로 최적화 (ASCII 256 기준)
    # 기본 점프 거리는 패턴의 길이 m
    skip = [m] * 256
    for i in range(m - 1):
        skip[ord(pattern[i])] = m - 1 - i
        
    results = []
    i = m - 1 # text의 현재 비교 위치
    while i < n:
        k = 0
        # 뒤에서부터 비교
        while k < m and pattern[m - 1 - k] == text[i - k]:
            k += 1
        
        if k == m: # 매칭 성공
            results.append(i - m + 2)
            # 매칭 성공 후 이동 (가장 단순하게 1칸 이동 혹은 lps 활용 가능)
            # 여기서는 안전하게 1칸 혹은 미리 계산된 값 활용
            i += 1 
        else:
            # 나쁜 문자 규칙에 따라 점프
            i += skip[ord(text[i])]
            
    return results

T=input()
P=input()
res = horspool(T,P)

print(len(res))
print(*(res))