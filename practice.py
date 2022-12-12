n = int(input())

ary = list(map(int, input().split()))

count = 0
check = True

while check:
  for i in range(n):
    if ary[i] % 2 == 0:
      ary[i] = ary[i] / 2
    else:
      check = False

  if check: count += 1

print(count)