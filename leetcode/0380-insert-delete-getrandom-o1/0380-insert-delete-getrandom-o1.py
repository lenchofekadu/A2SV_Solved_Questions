class RandomizedSet:

    def __init__(self):
        self.obj = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        temp = val in self.obj
        if not temp:
            self.lst.append(val)
            self.obj[val] = len(self.lst) - 1
        return not temp

    def remove(self, val: int) -> bool:
        if val in self.obj:
            idx = self.obj[val]
            self.lst[idx] = self.lst[-1]
            self.obj[self.lst[-1]] = idx
            self.lst.pop()
            del self.obj[val]
            return True

        return False

    def getRandom(self) -> int:
        return random.choice(self.lst)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()