s = input()
t = input()

result = 0
length = len(t)

s = list(s)
t = list(t)

s.append(" ")

for i in range(length):
  if s[i] != t[i]:
    result = i + 1
    break

print(result)