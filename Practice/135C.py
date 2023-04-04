N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = min(A[0], B[0])

# 最初の処理
if A[0] <= B[0]:
  B[0] -= A[0]
  A[0]  = 0
else:
  A[0] -= B[0]
  B[0]  = 0

for i in range(1, N + 1):
  # B[i - 1]が0じゃなかったらそっちを優先的に消費
  if B[i - 1] != 0:
    result += min(A[i], B[i - 1])

    if A[i] <= B[i - 1]:
      B[i - 1] -= A[i]
      A[i]      = 0
    else:
      A[i]     -= B[i - 1]
      B[i - 1]  = 0

    # B[i - 1]が0になっちゃってかつA[i]がまだ0じゃなかったら今度はB[i]を消費
    if (B[i - 1] == 0) and (A[i] != 0) and (i < N):
      result += min(A[i], B[i])

      if A[i] <= B[i]:
        B[i] -= A[i]
        A[i]  = 0
      else:
        A[i] -= B[i]
        B[i]  = 0
  else:
    result += min(A[i], B[i])

    if A[i] <= B[i]:
      B[i] -= A[i]
      A[i]  = 0
    else:
      A[i] -= B[i]
      B[i]  = 0

print(result)