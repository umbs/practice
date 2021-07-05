class Solution(object):
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        mid, ans = len(s)//2, 0

        for i in range(mid):
            if s[i] in vowels: ans += 1
            if s[mid+i] in vowels: ans -= 1

        return ans == 0

if __name__ == "__main__":
    s = Solution()
    print(s.halvesAreAlike("book"))
    print(s.halvesAreAlike("textbook"))
    print(s.halvesAreAlike("MerryChristmas"))
    print(s.halvesAreAlike("AbCdEfGh"))
