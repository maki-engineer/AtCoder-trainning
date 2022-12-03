n = int(input())
s = input().split(' ')

int_s  = [int(i) for i in s]
result = [int_s[0]]

for i in range(1, n):
  result.append(int_s[i] - sum(result))

result = [str(i) for i in result]
result = " ".join(result)
print(result)