lst = []
for i in range(5):
    lst += map(int, input().split())

row = lst.index(1) // 5 + 1
column = lst.index(1) % 5 + 1
print(abs(row - 3) + abs(column - 3))
