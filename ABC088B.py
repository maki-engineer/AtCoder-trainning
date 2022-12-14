N = int(input())
a = list(map(int, input().split()))

result = 0

a.sort(reverse=True)

for i in range(N):
  if i % 2 == 0:
    result += a[i]
  else:
    result -= a[i]

print(result)