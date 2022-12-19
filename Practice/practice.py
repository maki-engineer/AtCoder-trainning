A, B = map(int, input().split())

count = 0

for n in range(A, B + 1):
  num_str = str(n)

  if num_str[0] != num_str[-1]: continue
  if num_str[1] != num_str[-2]: continue

  count += 1

print(count)