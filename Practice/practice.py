A, B = map(int, input().split())

S = [A + B, A - B, A * B]

print(max(S))