# A問題
import math

N     = int(input())
count = 0

for n in range(N):
  S = input()

  if S == "For":
    count += 1

if count >= (math.ceil(N / 2)):
  print("Yes")
else:
  print("No")

# B問題
N, M = map(int, input().split())

S, T   = [], []
result = 0

for n in range(N):
  s = input()
  s = s[3:]
  S.append(s)

for m in range(M):
  t = input()
  T.append(t)

for s in S:
  if s in T:
    result += 1

print(result)

# C問題（不正解）
N, M = map(int, input().split())

G = [[] for n in range(N)]

count = 0

for m in range(M):
  u, v = map(int, input().split())

  G[u - 1].append(v - 1)
  G[v - 1].append(u - 1)

for g in G:
  if len(g) == 2:
    count += 1
  elif len(g) == 0:
    print("No")
    exit()

if count == len(G) - 2:
  print("Yes")
else:
  print("No")