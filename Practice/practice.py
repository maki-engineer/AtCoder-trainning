import numpy as np

N, K = map(int, input().split())

for i in range(K):

  N = "0O" + str(N)
  N = int(N, 0)
  N = np.base_repr(N, 9)

  b = ""

  n = list(str(N))

  for k in range(len(n)):
    if n[k] == "8":
      n[k] = "5"

    b += n[k]

  N = b

print(int(b))