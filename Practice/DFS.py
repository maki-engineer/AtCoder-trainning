import sys
sys.setrecursionlimit(10**7) # 再起回数の設定

H, W = map(int, input().split())
maze = [list(input()) for h in range(H)]

for h in range(H):
  for w in range(W):
    if maze[h][w] == "s":
      sx, sy = h, w

def dfs(x, y):
  # 範囲外や壁の場合は終了
  if y >= W or y < 0 or x >= H or x < 0 or maze[x][y] == '#':
    return

  # ゴールにたどり着ければ終了
  if maze[x][y] == 'g':
    print('Yes')
    exit()

  # 既に行ったルートは壁にしておく
  maze[x][y] = '#'

  # 上下左右への移動パターンで再起していく
  dfs(x + 1, y)
  dfs(x - 1, y)
  dfs(x, y + 1)
  dfs(x, y - 1)

# スタート地点から深さ優先探索
dfs(sx, sy)
print('No')