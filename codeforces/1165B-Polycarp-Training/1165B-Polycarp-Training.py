t = int(input())
lst = list(map(int, input().split()))

lst.sort()

count = 0
for i in lst:
    if i >= (count + 1):
        count += 1
print(count)