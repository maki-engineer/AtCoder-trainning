S = input()
N = len(S)

# 動的計画法用の配列
dp = [False] * (N + 1)

# 初期条件
dp[0] = True

for n in range(N + 1):
  if n >= 5 and dp[n - 5] and S[n - 5:n] == 'erase':
    dp[n] = True
  if n >= 6 and dp[n - 6] and S[n - 6:n] == 'eraser':
    dp[n] = True
  if n >= 5 and dp[n - 5] and S[n - 5:n] == 'dream':
    dp[n] = True
  if n >= 7 and dp[n - 7] and S[n - 7:n] == 'dreamer':
    dp[n] = True

print('YES' if dp[N] else 'NO')