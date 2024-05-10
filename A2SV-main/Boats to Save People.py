class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        small = 0
        large = len(people) - 1
        cont = 0
        while small <= large:
            if people[small] + people[large] == limit:
                cont += 1
                small += 1
                large -= 1
            elif people[small] + people[large] > limit:
                if people[large] > limit:
                    large -= 1
                else:
                    cont += 1
                    large -= 1

            elif people[small] + people[large] < limit:
                if people[small] > limit:
                    small += 1
                elif  people[small] + people[large] < limit:
                    cont += 1
                    small += 1
                    large -= 1
                else:
                    cont += 1
                    small += 1
        return cont
                
                
                
