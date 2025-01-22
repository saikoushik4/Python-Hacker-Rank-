n, m = map(int, input().split())
marks = []
for _ in range(m):
    marks.append(list(map(float, input().split())))
for i in range(n):
    avg = sum(marks[j][i] for j in range(m)) / m
    print(f"{avg:.1f}")
