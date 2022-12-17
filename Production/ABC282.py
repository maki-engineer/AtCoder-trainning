# A問題
K = int(input())

S = [chr(i) for i in range(65, 65 + K)]

print(''.join(S))

# B問題
N, M = map(int, input().split())

S = [input() for i in range(N)]

result = 0

for i in range(N):
  for j in range(i + 1, N):
    for k in range(M):
      if S[i][k] == 'x' and S[j][k] == 'x': break
      if k == M - 1: result += 1

print(result)

# C問題
N, S = int(input()), list(input())

search = 0

for n in range(N):
  if S[n] == '"':
    if search == 1:
      search = 0
    else:
      search = 1
  elif S[n] == ',':
    if search == 0: S[n] = '.'

print(''.join(S))