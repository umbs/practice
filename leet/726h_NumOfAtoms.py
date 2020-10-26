class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        ualph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lalph = "abcdefghijklmnopqrstuvwxyz"
        num = "23456789"
       
        def helper(formula, mul):
            if len(formula) == 0:
                return

            for i in range(len(formula)):
                if formula[i] in num:
                    key = str(formula[:i])
                    res[key] = res.get(key, 0) + int(formula[i])

    
    res = dict()
