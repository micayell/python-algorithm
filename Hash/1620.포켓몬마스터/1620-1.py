n, m = map(int, input().split())

name_to_id = {}
id_to_name = {}

for i in range(1, n + 1):
    name = input()
    name_to_id[name] = i
    id_to_name[str(i)] = name

for _ in range(m):
    q = input()

    if q.isdigit():
        print(id_to_name[q])

    else:
        print(name_to_id[q])
