# A問題
N, M = map(int, input().split())
A    = list(map(int, input().split()))
B    = list(map(int, input().split()))

result = 0

for b in B:
  result += A[b - 1]

print(result)

# B問題
N, K = map(int, input().split())
S    = list(input())

for n in range(N):
  if K == 0:
    S[n] = 'x'
  else:
    if S[n] == 'o':
      K -= 1

print(''.join(S))