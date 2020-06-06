class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        num = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                num += 1

        return num
