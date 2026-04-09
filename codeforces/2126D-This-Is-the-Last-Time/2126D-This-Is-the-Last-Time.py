t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    casino = []
    for _ in range(n):
        l, r, real = map(int, input().split())
        casino.append([l, r, real])

    casino.sort()

    
    for start, end, cash in casino:
        if start <= k <= end:
            k = max(k, cash)

    print(k)