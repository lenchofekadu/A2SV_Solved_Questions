n = int(input())
lst = list(map(int, input().split()))
lst.sort()

if n % 2 == 1:
    print(lst[n // 2])
else:
    print(lst[n // 2 - 1])