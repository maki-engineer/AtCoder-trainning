N = int(input())

result = 'Yes'

for i in range(N):
  T, x, y = map(int, input().split())

  # T < x + y ならば、絶対にその秒数でそこにたどり着けないため、強制的にNoで終了
  if T < (x + y):
    result = 'No'
    break

  # 偶数時
  if ((x + y) % 2 == 0) and (T % 2 == 0): continue

  # 奇数時
  if ((x + y) % 2 == 1) and (T % 2 == 1): continue

  result = 'No'
  break

print(result)