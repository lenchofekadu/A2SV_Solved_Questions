class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:

        x1 = s1.count("x")
        x2 = s2.count("x")
        y1 = s1.count("y") 
        y2 = s2.count("y")

        if (x1 + x2) % 2 != 0 or (y1 + y2) % 2 != 0:
            return -1

        xy, yx = 0, 0
        for first, sec in zip(s1, s2):
            if first == "x" and sec == "y":
                xy += 1
            elif first == "y" and sec == "x":
                yx += 1
        
        return xy // 2 + yx // 2 + 2 * (xy % 2)
        