# A問題
N = int(input())
S = [input() for n in range(N)]
S.reverse()

for s in S:
  print(s)

# B問題
T = int(input())

for t in range(T):
  count = 0
  N     = int(input())
  tests = list(map(int, input().split()))

  for test in tests:
    if test % 2 == 1:
      count += 1

  print(count)

# C問題
def dfs(v, G, seen):
    # 頂点 v を探索済みにする
    seen[v] = True
    # G[v] に含まれる頂点 v2 について、
    for v2 in G[v]:
        # v2 がすでに探索済みならば、スキップする
        if seen[v2]: continue
        # v2 始点で深さ優先探索を行う (関数を再帰させる)
        dfs(v2, G, seen)
    return

# 頂点数と辺の数
N, M = map(int, input().split())

# 頂点数Nのグラフを定義
G = [[] for n in range(N)]

# M本の辺を受け取る
for m in range(M):
  u, v = map(int, input().split())

  G[u - 1].append(v - 1)
  G[v - 1].append(u - 1)

seen   = [False for n in range(N)]
result = 0

for n in range(N):
  if seen[n]: continue
  dfs(n, G, seen)
  result += 1

print(result)

# D問題 失敗
def prime_factorize(n):
  a = []
  while n % 2 == 0:
    a.append(2)
    n //= 2
  f = 3
  while f * f <= n:
    if n % f == 0:
      a.append(f)
      n //= f
    else:
      f += 2
  if n != 1:
    a.append(n)
  return a

T = int(input())

for t in range(T):
  test = int(input())
  p, q = 0, 0
  pfs  = prime_factorize(test)

  for pf in pfs:
    if pfs.count(pf) == 2:
      p = pf
    else:
      q = pf

print(p, q)