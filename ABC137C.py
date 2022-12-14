N = int(input())
S = []

count = 0

for i in range(N):
  S.append(list(input()))
  S[i].sort()

S = list(map(''.join, S))

for i in range(1, N):
  for j in range(i):
    if S[i] == S[j]: count += 1

print(count)