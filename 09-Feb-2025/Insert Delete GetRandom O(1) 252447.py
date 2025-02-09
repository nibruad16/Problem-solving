# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.our_set = set()
        

    def insert(self, val: int) -> bool:
        already_there = val in self.our_set
        self.our_set.add(val)
        return not already_there
        

    def remove(self, val: int) -> bool:
        already_there = val in self.our_set
        self.our_set.discard(val)
        return already_there
        

    def getRandom(self) -> int:
        return random.choice(list(self.our_set))
        

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()