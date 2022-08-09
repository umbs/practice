class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        subs = {}
        idx = 0
        for c in key:
            if c == ' ':
                continue
            if c in subs:
                continue

            subs[c] = alpha[idx]
            idx += 1

        result = []
        for c in message:
            if c == ' ':
                result.append(c)
                continue

            result.append(subs[c])

        return ''.join(result)


if __name__ == "__main__":
    s = Solution()
    key = "the quick brown fox jumps over the lazy dog"
    message = "vkbs bs t suepuv"
    print(s.decodeMessage(key, message))
