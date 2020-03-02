"""
Pramp: Mar 2nd, 2020. Very simple problem. but I struggled to get it to work.
Following is solution from Pramp.
"""

def find_busiest_period(data):
    count, maxCount, maxTime = 0, 0, 0

    for i in range(len(data)):
        if data[i][2]:
            count += data[i][1]
        else:
            count -= data[i][1]

        if i+1 < len(data) and data[i][0] == data[i+1][0]:
            continue

        if maxCount < count:
            maxCount = count
            maxTime = data[i][0]

    return maxTime
