import sys

def get_skip_table(pattern):
    pattern_len = len(pattern)
    # skip_table[i]는 0부터 i까지의 부분 문자열 중 
    # 접두사와 접미사가 일치하는 최대 길이를 의미합니다.
    skip_table = [0] * pattern_len
    
    matched_len = 0 # 현재 일치한 접두사의 길이
    
    # 패턴의 두 번째 문자부터 끝까지 검사 (current_idx = 현재 비교할 접미사의 끝 인덱스)
    for current_idx in range(1, pattern_len):
        # 불일치할 경우, 이전 단계의 skip_table을 참조하여 매칭 길이를 줄여나감
        while matched_len > 0 and pattern[current_idx] != pattern[matched_len]:
            matched_len = skip_table[matched_len - 1]
        
        # 문자가 일치하면 매칭된 길이를 1 늘리고 테이블에 저장
        if pattern[current_idx] == pattern[matched_len]:
            matched_len += 1
            skip_table[current_idx] = matched_len
            
    return skip_table

def kmp_search(entire_text, search_pattern):
    text_len = len(entire_text)
    pattern_len = len(search_pattern)
    
    skip_table = get_skip_table(search_pattern)
    match_indices = [] # 찾은 위치들을 저장할 리스트
    
    pattern_ptr = 0 # 패턴을 가리키는 포인터 (현재까지 매칭된 길이이기도 함)
    
    # 본문의 처음부터 끝까지 한 글자씩 확인 (text_idx = 본문의 현재 위치)
    for text_idx in range(text_len):
        # 현재 문자가 패턴과 다르면, skip_table을 이용해 pattern_ptr를 이동
        while pattern_ptr > 0 and entire_text[text_idx] != search_pattern[pattern_ptr]:
            pattern_ptr = skip_table[pattern_ptr - 1]
            
        # 문자가 일치하는 경우
        if entire_text[text_idx] == search_pattern[pattern_ptr]:
            # 패턴의 마지막 글자까지 모두 일치했다면?
            if pattern_ptr == pattern_len - 1:
                # 시작 인덱스를 계산하여 결과 리스트에 추가 (1-indexed)
                match_indices.append(text_idx - pattern_len + 2)
                # 다음 매칭을 위해 skip_table을 참조하여 포인터 이동
                pattern_ptr = skip_table[pattern_ptr]
            else:
                # 아직 패턴 진행 중이라면 다음 칸으로 이동
                pattern_ptr += 1
                
    return match_indices

# 백준 1786번은 공백을 포함할 수 있으므로 sys.stdin.readline 사용 권장
entire_text = sys.stdin.readline().rstrip('\n')
search_pattern = sys.stdin.readline().rstrip('\n')

found_positions = kmp_search(entire_text, search_pattern)

# 결과 출력
print(len(found_positions))
print(*(found_positions))