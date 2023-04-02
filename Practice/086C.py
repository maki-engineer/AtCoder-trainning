N = int(input())

result = 'Yes'

pt, px, py = 0, 0, 0

for i in range(N):
  t, x, y = map(int, input().split())
  T, X, Y = t - pt, abs(x - px), abs(y - py)

  # T < x + y ならば、絶対にその秒数でそこにたどり着けないため、強制的にNoで終了
  if T < (X + Y):
    result = 'No'
    break

  if (T % 2) != ((X + Y) % 2):
    result = 'No'
    break

  pt, px, py = t, x, y

print(result)