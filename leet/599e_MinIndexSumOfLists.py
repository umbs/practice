"""
TC: O(m+n), SC: O(n)
m = len(list1)
n = len(list2)
"""

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        h2 = dict()
        
        for i in range(len(list2)):
            h2[list2[i]] = i
        
        less = len(list1) + len(list2)
        res = list()
        
        for i in range(len(list1)):
            tmp = h2.get(list1[i], 2*less)
            if tmp+i < less:
                del res
                res = list()
                res.append(list1[i])
                less = tmp + i
            elif tmp+i == less:
                res.append(list1[i])
        
        return res
