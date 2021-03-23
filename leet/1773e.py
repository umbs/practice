class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        idx = ["type", "color", "name"].index(ruleKey)
        res = 0
        for it in items:
            if it[idx] == ruleValue:
                res += 1
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]],
        "color", "silver"))
    print(s.countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]],
        "type", "phone"))
