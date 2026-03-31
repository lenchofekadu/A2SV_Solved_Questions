class RandomizedSet:

    def __init__(self):
        self.obj = set()
        self.lst = []

    def insert(self, val: int) -> bool:
        temp = val in self.obj
        if not temp:
            self.obj.add(val)
            self.lst.append(val)
        return not temp

    def remove(self, val: int) -> bool:
        if val in self.obj:
            self.obj.remove(val)
            self.lst.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.lst)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()