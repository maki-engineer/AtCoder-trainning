H, W = map(int, input().split())

if H == 1 or W == 1:
  print(H * W)
  exit()

if H % 2 != 0:
  H += 1

if W % 2 != 0:
  W += 1

print(int((W / 2) * (H / 2)))