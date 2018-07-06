class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines, current_width = 1, 0

        for c in S:
            required_width = widths[ord(c) - ord('a')]

            if required_width > 100:
                return 0, 0

            # c can NOT fit in remaining space, start a new line
            if required_width > 100-current_width:
                current_width = required_width
                lines += 1
            else:
                current_width += required_width

        return lines, current_width

"""
widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"
"""

widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "bbbcccdddaaa"

sol = Solution()

print sol.numberOfLines(widths, S)
