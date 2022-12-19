import numpy as np

N, K = map(int, input().split())

while K > 0:
    N = "0O" + str(N)
    N = int(N,0)
    b = ""
    N = np.base_repr(N, 9)
    n = list(str(N))
    for i in range(len(n)):
        if n[i] == "8":
            n[i] = "5"
        b += n[i]
    N = b
    K -= 1
print(int(b))