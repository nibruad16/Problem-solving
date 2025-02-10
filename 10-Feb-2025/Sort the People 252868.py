# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        new = sorted(zip(heights,names),reverse=True)
        return [name for height,name in new]




        # for i in range(len(names)):
        #     swap = False
        #     for j in range(len(names)- i- 1):
        #         if heights[j] < heights[j+1]:
        #             heights[j], heights[j+1] = heights[j+1],heights[j]
        #             names[j] , names[j+1] = names[j+1] , names[j]
        #             swap = True
        #     if not swap:
        #         break
        # return names


        
