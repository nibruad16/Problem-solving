class Solution: 
    def select(self, arr, i):
        
        mi = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[mi]:
                mi = j
        return mi
    
    def selectionSort(self, arr,n):
        
        for i in range(n-1):
            small = self.select(arr, i)
            arr[i], arr[small] = arr[small], arr[i]
