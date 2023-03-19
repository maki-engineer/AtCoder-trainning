# A問題
N = int(input())
A = list(map(int, input().split()))
results = []

for a in A:
  if a % 2 == 0:
    results.append(a)

print(*results)

# B問題
H, W = map(int, input().split())

for h in range(H):
  maps    = map(int, input().split())
  results = []

  for num in maps:
    if num == 0:
      results.append(".")
    else:
      results.append(chr(num + 64))

  print("".join(results))

# C問題 不正解
N, M = map(int, input().split())
A    = list(map(int, input().split()))
B    = list(map(int, input().split()))
C    = A + B

# Cを昇順にソート
C = sorted(C)

A_index = [C.index(A[n]) + 1 for n in range(N)]
B_index = [C.index(B[m]) + 1 for m in range(M)]

print(*A_index)
print(*B_index)