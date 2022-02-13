import numpy as np

def maxpoint(a, b, c):
    dp = np.zeros((a + 100, b + 100, c + 100))
    for i in range(a, -1, -1):    # Design DP function
        for j in range(b, -1, -1):
            for k in range(c, -1, -1):
                #rule 1  500 points
                if i + 75 <= a and j + 25 <= b and k + 25 <=c:
                    if dp[i + 75][j + 25][k + 25] + 500 > dp[i][j][k]:
                        dp[i][j][k] = dp[i + 75][j + 25][k + 25] + 500
                #rule 2  300 points
                if i + 75 <= a and j + 25 <= b:
                    if dp[i + 75][j + 25][k] + 300 > dp[i][j][k]:
                        dp[i][j][k] = dp[i + 75][j + 25][k] + 300
                #rule 3  200 points
                if i + 75 <= a:
                    if dp[i + 75][j][k] + 200 > dp[i][j][k]:
                        dp[i][j][k] = dp[i + 75][j][k] + 200
                #rule 4  150 points
                if i + 25 <= a and j + 10 <= b and k + 10 <=c:
                    if dp[i + 25][j + 10][k + 10] + 150 > dp[i][j][k]:
                        dp[i][j][k] = dp[i + 25][j + 10][k + 10] + 150
                #rule 5  75 points
                if i + 25 <= a and j + 10 <= b:
                    if dp[i + 25][j + 10][k] + 75 > dp[i][j][k]:
                        dp[i][j][k] = dp[i + 25][j + 10][k] + 75
                #rule 6  75 points
                if i + 20 <= a:
                    if dp[i + 20][j][k] + 75 > dp[i][j][k]:
                        dp[i][j][k] = dp[i + 20][j][k] + 75
                #rule 7 i+j+k  1 points

    max_point = 0
    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                max_point = max(dp[i][j][k] + i+j+k, max_point)
    return max_point