# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #optial
        # new = sorted(zip(heights,names),reverse=True)
        # return [name for height,name in new]

        # counting Sort 

        me = heights.copy()
        max_num = max(heights)
        count = [0] * (max_num + 1)
        for num in heights:
            count[num] += 1
        ans = []
        target = 0
        for index,val in enumerate(count):
            for i in range(val):
                heights[target] = index
                temp = me.index(index)
                ans.append(names[temp])
                target += 1
        ans.reverse()
        return ans


        # insertion sort
        # for i in range(1,len(names)):
        #     key = heights[i]
        #     nkey = names[i]
        #     j = i - 1

        #     while j >= 0  and key > heights[j]:
        #         heights[j+1] = heights[j]
        #         names[j+1] = names[j]
        #         j -= 1
        #     heights[j+1] = key 
        #     names[j+1] = nkey

        # return names

        # selection sort 
        # for i in range(len(names)):
        #     mini = i
        #     for j in range(i+1,len(names)):
        #         if heights[mini] < heights[j]:
        #             mini = j

                #     heights[i],heights[mini] = heights[mini],heights[i]
                #     names[i],names[mini] = names[mini] , names[i]
        # return names



        # bubbel sort 
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


        
