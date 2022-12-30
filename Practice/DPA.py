import sys
sys.setrecursionlimit(10**7) # 再起回数の設定

N = int(input())
H = list(map(int, input().split()))

# 十分大きい値
INF = 10 ** 60

# 動的計画法用の配列
dp = [-1] * N

def rec(n):
  if n == 0:
    return 0

  # 既に計算済みだったら、その値を返す
  if dp[n] != -1:
    return dp[n]

  result = INF

  # 頂点の1個前から来た場合
  if n - 1 >= 0:
    result = min(result, rec(n - 1) + abs(H[n] - H[n - 1]))

  # 頂点の2個前から来た場合
  if n - 2 >= 0:
    result = min(result, rec(n - 2) + abs(H[n] - H[n - 2]))

  # 答えをdpにメモしながら返す
  dp[n] = result
  print(result, dp)
  return result

print(rec(N - 1))