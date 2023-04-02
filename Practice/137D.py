N, M = map(int, input().split())
jobs = [list(map(int, input().split())) for _ in range(N)]

# 報酬
result = 0

# 日数
date = 0

# 報酬が貰える日数が多い順に並び替える
jobs = sorted(jobs, key=lambda x: (x[1], x[0]), reverse=True)

# 貧欲法を使って求めていく
while True:
  for i in range(len(jobs)):
    if (date + jobs[i][0]) <= M:
      result += jobs[i][1]
      jobs.pop(i)
      break
  else:
    break

  date += 1

print(result)