class Solution(object):
    def kidsWithCandies(self, candies, ec):
        out = []
        big = max(candies)
        for i in candies:
            if i + ec >= big:
                out.append(True)
            else:
                out.append(False)
        
        return out
