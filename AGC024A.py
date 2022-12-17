A, B, C, K = map(int, input().split())

if abs(A - B) > (10 ** 18):
  print('Unfair')
else:
  print(A - B if K % 2 == 0 else B - A)