# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:
    def __init__(self):
        self.presum = []
        self.presum.append(1)
    def add(self, num: int) -> None:
        if num == 0:
            self.presum = [1]
        else:
            self.presum.append(self.presum[-1] * num)
            
    def getProduct(self, k: int) -> int:
        return self.presum[-1] // self.presum[-k-1] if k < len(self.presum) else 0
      
    
        

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)