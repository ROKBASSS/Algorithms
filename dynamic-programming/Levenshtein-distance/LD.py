a = input()
b = input()

def LD(A: list, B: list):
    """
    """
    n, m = len(A), len(B)
    dp = []
    for i in range(n+1):
        dp.append([0]*(m+1))

    for i in range(1, n+1):
        dp[i][0] = i

    for j in range(1, m+1):
        dp[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = min(dp[i-1][j-1] + (a[i-1] != b[j-1]),
                           dp[i][j-1]+1, dp[i-1][j] + 1)
    return dp

dp = LD(a,b)
print(dp[-1][-1])
