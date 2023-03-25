# A問題
N = int(input())
W = list(input().split())

checks = ["and", "not", "that", "the", "you"]

for w in W:
  if w in checks:
    print("Yes")
    exit()

print("No")