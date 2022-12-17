A, B, C, K = map(int, input().split())

print('Unfair') if abs(A - B) > (10 ** 18) else print(A - B if K % 2 == 0 else B - A)