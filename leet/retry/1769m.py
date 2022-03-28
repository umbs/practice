class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)
        ops, cnt = 0, 0
        for i in range(len(boxes)):
            ans[i] += ops
            cnt += int(boxes[i])
            ops += cnt

        ops, cnt = 0, 0
        for i in reversed(range(len(boxes))):
            ans[i] += ops
            cnt += int(boxes[i])
            ops += cnt
        
        return ans
