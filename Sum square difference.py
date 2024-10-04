t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum_of_sq = n * (n + 1) * (2 * n + 1) / 6
    sq_of_sum = (n * (1 + n) / 2) ** 2
    print(int(abs(sum_of_sq - sq_of_sum)))
