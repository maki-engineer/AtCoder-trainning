# A問題
N = int(input())

result = 'L'

for _ in range(N):
    result += 'o'

result += 'ng'

print(result)


# B問題
N = int(input())

N = bin(N)[2:]
result = 0


if N[-1] == '1':
    print(result)
else:
    index_num = -1

    while True:
        if N[index_num] == '0':
            result += 1
            index_num -= 1
        else:
            break

    print(result)


# C問題（不正解）
N = int(input())

search_num = 0
found_target_num = 0
result = 0
odd_nums = ['1', '3', '5', '7', '9']

while True:
    if found_target_num == N:
        break

    # search_numが全て偶数かどうか
    for odd_num in odd_nums:
        # もしsearch_numの中に奇数が含まれている場合、含まれていた場所を足すようにする
        odd_search_index = str(search_num).find(odd_num)
        if odd_search_index != -1:
            search_num_to_list = list(str(search_num))
            if search_num_to_list[odd_search_index] == '9':
                if odd_search_index == 0:
                    search_num_to_list[odd_search_index] = '0'
                    search_num_to_list.insert(0, '1')
                    search_num = int(''.join(search_num_to_list))
                else:
                    search_num_to_list[odd_search_index] = '0'
                    search_num_to_list[odd_search_index - 1] = str(int(search_num_to_list[odd_search_index - 1]) + 1)
                    search_num = int(''.join(search_num_to_list))
            else:
                search_num_to_list[odd_search_index] = str(int(search_num_to_list[odd_search_index]) + 1)
                search_num = int(''.join(search_num_to_list))

            break
    else:
        found_target_num += 1
        result = search_num
        search_num += 2

print(result)

