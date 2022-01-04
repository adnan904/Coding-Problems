if __name__ == '__main__':
    str1 = "voldemort"
    str2 = "dumbledore"
    DP = [[0]*(len(str1) + 1) for _ in range(2)]
    for i in range(1, len(str1) + 1):
        DP[0][i] = i
    for i in range(1, len(str2) + 1):
        DP[i % 2][0] = i
        for j in range(1, len(str1) + 1):
            if str2[i-1] == str1[j-1]:
                DP[i % 2][j] = DP[(i - 1) % 2][j-1]
            else:
                DP[i % 2][j] = 1 + min(DP[(i - 1) % 2][j-1], DP[(i - 1) % 2][j], DP[i % 2][j-1])
    print(DP[len(str2) % 2][len(str1)])
