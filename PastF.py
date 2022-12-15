S = input()
N = len(S)
i = 0

words = []
count = 0

while i < N:
  j = i

  while j < N:
    if S[j].isupper(): count += 1

    j += 1

    if count == 2:
      count = 0
      break

  words.append(S[i:j])

  i = j

words = [word.lower() for word in words]

words.sort()

for i in range(len(words)):
  ary      = list(words[i])
  ary[0]   = words[i][0].upper()
  ary[-1]  = words[i][-1].upper()
  words[i] = ''.join(ary)

print(*words, sep='')