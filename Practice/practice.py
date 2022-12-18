H, W = map(int, input().split())

S = [['.'] * W for i in range(H)]

result = 0

for h in range(H):
  for w in range(W):
    if h % 2 == 0:
      if w % 2 == 0:
        result += 1

print(result)