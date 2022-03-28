class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for string in strs:
            sort_string = ''.join(sorted(string))
            if sort_string in ans:
                ans[sort_string].append(string)
            else:
                ans[sort_string] = [string]
            
        
        return list(ans.values())
