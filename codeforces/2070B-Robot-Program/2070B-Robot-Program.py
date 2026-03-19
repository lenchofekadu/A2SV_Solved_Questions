t = int(input())

for _ in range(t):
    n, x, k = map(int, input().split())

    s = input()
    large = 0 
    ans, step, count = None,  0, 0

    for j, i in enumerate(s):
        if i == "L":
            count -= 1
        else:
            count += 1
    
        if count == 0:
          
            if not step:
                step = j + 1
        
        if k - j - 1 >= 0 and x + count == 0:
            if not ans:
                ans = j + 1
  
    if not ans:
        print(0)
        continue
    
    if not step:
        print(1)
    
    else:
        left = k - ans

        print(1 + left // step)