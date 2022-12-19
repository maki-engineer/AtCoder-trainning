def base10int(value, base):
  if (int(value / base)):
    return base10int(int(value / base), base) + str(value % base)
  return str(value % base)

N, K = map(str, input().split())
N    = int(N, 8)
K    = int(K)

for i in range(K):
  N = base10int(N, 9)
  N = N.replace('8', '5')
  N = int(N, 8)

N = base10int(N, 8)

print(N)