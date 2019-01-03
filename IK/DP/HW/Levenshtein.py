def small(a, b, c):
    return min(a, min(b, c))


def  levenshteinDistance(w1, w2):
    row, col = len(w1), len(w2)
    dp = [[row+col for j in range(col+1)] for i in range(row+1)]

    for i in range(0, row+1):
        dp[i][0] = i

    for i in range(0, col+1):
        dp[0][i] = i


    for i in range(1, row+1):
        for j in range(1, col+1):
            if w1[i-1] == w2[j-1]:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1])
            else:
                dp[i][j] = min(dp[i][j],
                            1 + small(dp[i-1][j-1], # Replace
                                      dp[i-1][j],  # Insert
                                      dp[i][j-1]) # Remove
                              )

    return dp[row][col]


if __name__ == "__main__":
    # print(levenshteinDistance("kitten", "sitten"))
    # print(levenshteinDistance("cat", "bat"))
    print(levenshteinDistance("pizza", "yolo"))
