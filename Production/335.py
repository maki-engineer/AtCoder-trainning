# A問題
S = list(input())

S[-1] = '4'

print(''.join(S))

# B問題
N = int(input())

xyz = [0, 0, 0]

for x in range(N + 1):
    for y in range(N + 1):
        for z in range(N + 1):
            if (x + y + z) <= N:
                print(f'{x} {y} {z}')
            else:
                break

# C問題
