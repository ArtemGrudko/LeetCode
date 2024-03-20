import random
# Вы поднимаетесь по лестнице. Чтобы достичь вершины, требуется n ступенек.
# Каждый раз вы можете подняться либо на 1, либо на 2 ступеньки. Сколькими различными способами вы можете подняться на вершину?


def generate_dataset(min_val, max_val):
    return random.randint(min_val, max_val)

def climbStairs(n):
    if n == 0 or n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

min_val = 1
max_val = 50

n = generate_dataset(min_val, max_val)
print("num of the steps:", n)

result = climbStairs(n)
print("number of ways:", result)
