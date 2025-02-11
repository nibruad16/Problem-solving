# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

#User function Template for python3

class Solution: 
    def selectionSort(self, arr):
        
        for i in range(len(arr)):
            mini = i
            for j in range(i+1,len(arr)):
                if arr[mini] > arr[j]:
                    mini = j
            arr[i],arr[mini] = arr[mini],arr[i]
        return arr

