N = int(input())
v = list(map(int, input().split()))

for _ in range(N - 1):
  min_num = 2001
  first_i = -1
  sec_i   = -1

  # 2つの差が一番少ない組み合わせを合成する
  for j in range(len(v)):
    for k in range(len(v)):
      if j == k: continue

      if v[j] + v[k] < min_num:
        min_num = v[j] + v[k]
        first_i = j
        sec_i   = k

  # 最も差が少ない2つの要素を削除して、新しい具材を追加する
  v.pop(first_i)
  v.pop(sec_i - 1)
  v.append(min_num / 2)

print(v[0])