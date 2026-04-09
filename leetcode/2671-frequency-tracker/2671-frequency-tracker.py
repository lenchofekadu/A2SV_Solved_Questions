class FrequencyTracker:

    def __init__(self):
        self.count = Counter()
        self.freq = Counter()

    def add(self, number: int) -> None:
        prev = self.count[number]
        new = prev + 1
        self.count[number] = new

    
        self.freq[prev] -= 1
        
        self.freq[new] += 1

    def deleteOne(self, number: int) -> None:
        freq_of_to_be_deleted_num = self.count[number]
        new = freq_of_to_be_deleted_num - 1
        if self.count[number] > 0:
            self.count[number] -= 1
        
        self.freq[freq_of_to_be_deleted_num] -= 1
        self.freq[new] += 1
    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)