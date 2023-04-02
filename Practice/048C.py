N, x = map(int, input().split())
a    = list(map(int, input().split()))

count = 0

for i in range(N - 1):
  # その場所の飴の個数がxより上なら食べる
  if a[i] > x:
    num    = a[i] - x
    a[i]  -= num
    count += num

  # 合計値がxより上なら食べる
  if a[i] + a[i + 1] > x:
    num       = (a[i] + a[i + 1]) - x
    a[i + 1] -= num
    count    += num

print(count)