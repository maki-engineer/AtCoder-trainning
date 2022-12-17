from collections import defaultdict

N = int(input())
S = []

num = defaultdict(int)

count = 0

for i in range(N):
  S.append(list(input()))
  S[i].sort()

S = list(map(''.join, S))

for s in S:
  num[s] += 1

for key in num:
  count += (num[key] * (num[key] - 1)) // 2

print(count)