h, w  = map(int, input().split())
count = 0

for i in range(h):
  maps = input()
  maps = list(maps)

  for i2 in range(w):
    if maps[i2] == '#': count += 1

print(count)