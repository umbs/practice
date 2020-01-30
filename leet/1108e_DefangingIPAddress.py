class Solution(object):
    def defangIPaddr(self, address):
        return address.replace(".", "[.]")


S = Solution()
print S.defangIPaddr("1.1.1.1")
print S.defangIPaddr("255.100.50.0")
