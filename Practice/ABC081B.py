n = int(input())
a = list(map(int, input().split()))

count = 0
check = False

while True:
  for i in range(n):
    if a[i] % 2 == 0:
      a[i] //= 2
    else:
      check = True
      break

  if check:
    break
  else:
    count += 1

print(count)