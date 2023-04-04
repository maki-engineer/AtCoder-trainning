n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

R = 0

for i in range(n):
  if A[i] > B[i]:
    R += B[i]
  else:
    R    += A[i]
    B[i] -= A[i]
    if A[i + 1] > B[i]:
      R      += B[i]
      A[i + 1] -= B[i]
    else:
      R       += A[i + 1]
      A[i + 1] =0

print(R)