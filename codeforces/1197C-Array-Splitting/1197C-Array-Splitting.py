n, k = map(int, input().split())

lst = list(map(int, input().split()))

cuts = []

for i in range(1, n):
    cuts.append(lst[i] - lst[i - 1])

cuts.sort(reverse=True)

total = sum(cuts[:k - 1])

diff = max(lst) - min(lst)

print(diff - total)