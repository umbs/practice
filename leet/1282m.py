class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result, run = [], {}
        
        for idx, val in enumerate(groupSizes):
            group = run.get(val, [])
            group.append(idx)
            
            if len(group) == val:   # group has reached it's limit
                result.append(group)
                run[val] = []
            else:                   # There's room in group. Update it
                run[val] = group
            
        
        return result
