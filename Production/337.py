# A問題
N = int(input())
takahashi = 0
aoki = 0

for _ in range(N):
    x, y = map(int, input().split())
    takahashi += x
    aoki += y


if takahashi == aoki:
    print('Draw')
elif takahashi < aoki:
    print('Aoki')
else:
    print('Takahashi')


# B問題
S = input()

if len(S) < 2:
    print('Yes')
    exit()

a = ''
b = ''
c = ''

for s in S:
    if s == 'A':
        a += s
    elif s == 'B':
        b += s
    else:
        c += s

result = a + b + c

print('Yes' if result == S else 'No')


# C問題
N = int(input())
A = list(map(int, input().split()))

result = []

for i in range(N):
    if A[i] == -1:
        result.append(i + 1)
        break

while len(result) != len(A):
    result.append(A.index(result[-1]) + 1)

print(' '.join(map(str, result)))


# D問題
