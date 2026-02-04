# 1,6
# Musinsa,3
# S,160,170,85,95,70,80
# M,165,175,90,100,75,85
# L,170,180,95,105,80,90
# Musinsa,160,94,80
# Musinsa,175,95,85
# Nike,170,96,80
# Musinsa,182,106,91
# Musinsa,155,80,61
# Musinsa,180,95,70


import sys

# 1. 브랜드 수(N)와 쿼리 수(Q) 입력
# 예: 1, 6 -> N=1, Q=6
n_str, q_str = input("브랜드 수와 검색 횟수 입력 (ex: 1, 6): ").split(',')
N, Q = int(n_str), int(q_str)

brand_db = {}

# 2. 브랜드 데이터 입력 (N번 반복)
for _ in range(N):
    # 예: Musinsa, 3
    brand_info = input("\n브랜드명, 사이즈 개수 (ex: Musinsa, 3): ").split(',')
    brand_name = brand_info[0].strip()
    size_count = int(brand_info[1])
    
    brand_db[brand_name] = {}
    
    # 사이즈별 상세 데이터 입력
    for _ in range(size_count):
        # 예: S, 160, 170, 85, 95, 70, 80
        data = input("사이즈명, 키min, 키max, 가슴min, 가슴max, 허리min, 허리max: ").split(',')
        s_name = data[0].strip()
        # 데이터를 숫자형(int)으로 변환하여 저장
        brand_db[brand_name][s_name] = {
            "height": (int(data[1]), int(data[2])),
            "chest": (int(data[3]), int(data[4])),
            "waist": (int(data[5]), int(data[6]))
        }

print("\n" + "="*40)
print("🔍 검색을 시작합니다.")

# 3. 쿼리 처리 (Q번 반복)
for i in range(Q):
    # 예: Musinsa, 160, 94, 80
    query = input(f"검색 {i+1}: ").split(',')
    target_brand = query[0].strip()
    h, c, w = int(query[1]), int(query[2]), int(query[3])
    
    # 플래그(Flag) 사용: 브랜드 존재 여부 확인
    if target_brand not in brand_db:
        print(f"결과: {target_brand} 브랜드 정보가 없습니다.")
        continue
    
    found_size = "해당 없음"
    
    # 해당 브랜드 내의 사이즈들을 돌면서 범위 체크
    for size_name, specs in brand_db[target_brand].items():
        # 모든 부위가 최소~최대 범위 안에 있는지 확인
        if (specs["height"][0] <= h <= specs["height"][1] and
            specs["chest"][0] <= c <= specs["chest"][1] and
            specs["waist"][0] <= w <= specs["waist"][1]):
            found_size = size_name
            break # 적합한 사이즈를 찾으면 중단
            
    print(f"결과: {target_brand} - 추천 사이즈: {found_size}")