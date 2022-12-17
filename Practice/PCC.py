N = int(input())

T, c1, c2, c3 = 0, 0, 0, 0

for i in range(N):
  S = input()

  # まず最初にABが何個含まれているか
  T += S.count('AB')

  # パターン1
  if S[0] == 'B' and S[-1] == 'A':
    c1 += 1
  # パターン2
  elif S[-1] == 'A':
    c2 += 1
  # パターン3
  elif S[0] == 'B':
    c3 += 1

if c2 == 0 and c3 == 0:
  print(T + max(c1 - 1, 0))
else:
  print(T + c1 + min(c2, c3))