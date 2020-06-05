class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        sec = 0
        for i in range(len(points)-1):
            sec += max(abs(points[i][0]-points[i+1][0]), abs(points[i][1]-points[i+1][1]))
        return sec
