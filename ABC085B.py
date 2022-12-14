N = int(input())
D = []

for n in range(N):
  D.append(int(input()))

D.sort(reverse=True)

i      = 1
result = [D[0]]

for n in range(1, N):
  if result[n - i] > D[n]:
    result.append(D[n])
  else:
    i += 1

print(len(result))