"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
"""
Solution from: https://leetcode.com/problems/employee-importance/discuss/112611/3-liner-Python-Solution-(beats-99)
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        
        emp = {e.id: e for e in employees}
        
        def dfs(id):
            tot = emp[id].importance
            for s in emp[id].subordinates:
                tot += dfs(emp[s].id)
            return tot
        
        return dfs(id)
