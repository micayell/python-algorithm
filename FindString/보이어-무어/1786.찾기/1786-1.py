import sys

def precompute_bad_char(pattern):
    """나쁜 문자 테이블 생성"""
    bad_char = {}
    m = len(pattern)
    for i in range(m):
        bad_char[pattern[i]] = i
    return bad_char

def precompute_good_suffix(pattern):
    """착한 접미사 테이블 생성"""
    m = len(pattern)
    suffix = [0] * (m + 1)
    f = [0] * (m + 1)
    
    # Case 1: 패턴 내부에서 일치하는 접미사 찾기
    i = m
    j = m + 1
    f[i] = j
    while i > 0:
        while j <= m and pattern[i-1] != pattern[j-1]:
            if suffix[j] == 0:
                suffix[j] = j - i
            j = f[j]
        i -= 1
        j -= 1
        f[i] = j
        
    # Case 2: 접두사와 일치하는 접미사 처리 (가장 긴 경계 활용)
    j = f[0]
    for i in range(m + 1):
        if suffix[i] == 0:
            suffix[i] = j
        if i == j:
            j = f[j]
            
    return suffix

def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0: return []
    
    bad_char = precompute_bad_char(pattern)
    good_suffix = precompute_good_suffix(pattern)
    
    results = []
    shift = 0
    while shift <= n - m:
        j = m - 1
        # 오른쪽에서 왼쪽으로 비교
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1
            
        if j < 0:
            # 패턴을 찾은 경우
            results.append(shift + 1)
            shift += good_suffix[0]
        else:
            # 불일치 발생 시 두 규칙 중 최대값만큼 이동
            char_at_text = text[shift + j]
            bc_shift = j - bad_char.get(char_at_text, -1)
            gs_shift = good_suffix[j + 1]
            shift += max(bc_shift, gs_shift)
            
    return results

# 입력 처리
T = sys.stdin.readline().rstrip('\n')
P = sys.stdin.readline().rstrip('\n')

ans = boyer_moore(T, P)

# 결과 출력
print(len(ans))
print(*(ans))