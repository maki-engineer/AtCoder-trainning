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

words.sort(key=str.lower)

print(*words, sep='')