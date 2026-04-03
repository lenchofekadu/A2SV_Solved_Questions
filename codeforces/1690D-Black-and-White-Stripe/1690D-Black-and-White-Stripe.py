t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    white = s[:k].count("W")
    left, right = 0, k 
    res = white
    while right < n:
        if s[right] == "W":
            white += 1
        if s[left] == "W":
            white -= 1

        res = min(res, white)
        left += 1
        right += 1
    print(res)