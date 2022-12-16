N, M, Q = map(int, input().split())

maps = [[] for i in range(N)]

for i in range(M):
  u, v = map(int, input().split())

  maps[u - 1].append(v - 1)
  maps[v - 1].append(u - 1)

colors = list(map(int, input().split()))

for i in range(Q):
  query = list(map(int, input().split()))

  if query[0] == 1:
    print(colors[query[1] - 1])

    # 隣接する全ての頂点の色を塗り替える
    for m in maps[query[1] - 1]:
      colors[m] = colors[query[1] - 1]

  else:
    print(colors[query[1] - 1])

    colors[query[1] - 1] = query[2]