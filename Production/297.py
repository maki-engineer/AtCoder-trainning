# A問題
N, D = map(int, input().split())
T    = list(map(int, input().split()))

for i in range(N - 1):
  if T[i + 1] - T[i] <= D:
    print(T[i + 1])
    break
else:
  print(-1)

# B問題
S = input()

B_index         = []
is_middle       = False
is_second_check = False

for i in range(len(S)):
  # Bを配列に格納していく
  if S[i] == 'B':
    B_index.append(i + 1)

  # Rがあったら
  if S[i] == 'R':
    if is_middle:
      is_middle = False
    else:
      is_middle = True

  # K があったら
  if S[i] == 'K':
    if is_middle:
      is_second_check = True

if not is_second_check:
  print('No')
  exit()

if (B_index[0] + B_index[1]) % 2 == 0:
  print('No')
  exit()

print('Yes')

# C問題(不正解)
H, W = map(int, input().split())
S    = [list(input()) for _ in range(H)]

for h in range(H):
  for w in range(W - 1):
    if S[h][w] == 'T' and S[h][w + 1] == 'T':
      S[h][w]     = 'P'
      S[h][w + 1] = 'C'

for s in S:
  print(''.join(s))

# D問題
A, B = map(int, input().split())

count = 0

while A != B:
  # もし2つの数が割り切れそうだったらその割った数から1引いた数をcountに足して終了
  if A > B:
    if A % B == 0:
      count += (A // B) - 1
      A      = A - (B * ((A // B) - 1))
    else:
      count += A // B
      A      = A - (B * (A // B)) 
  else:
    if B % A == 0:
      count += (B // A) - 1
      B      = B - (A * ((B // A) - 1))
    else:
      count += B // A
      B      = B - (A * (B // A))

print(count)
