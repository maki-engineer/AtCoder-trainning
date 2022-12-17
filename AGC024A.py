A, B, C, K = map(int, input().split())

ary = [0, 0, 0]

if abs(A - B) > (10 ** 18):
  print('Unfair')
else:
  if K % 2 == 0:
    print(A - B)
  else:
    ary[0] = B + C
    ary[1] = A + C
    ary[2] = A + B

    print(ary[0] - ary[1])