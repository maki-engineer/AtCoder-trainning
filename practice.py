n, a, b = map(int, input().split())
data    = []

for i in range(1, n + 1):
  s   = str(i)
  ary = list(map(int, s))

  if a <= sum(ary) <= b: data.append(i)

print(sum(data))
