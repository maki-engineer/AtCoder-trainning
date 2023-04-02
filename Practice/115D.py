N, X = map(int, input().split())

def make_burger(N):
  str = ''

  if N == 0:
    str += 'P'
    return str

  str += 'B' + make_burger(N - 1) + 'P' + make_burger(N - 1) + 'B'
  return str

data = make_burger(N)

print(data)
data = data[:X]

result = data.count('P')

print(result)