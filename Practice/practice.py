N, A = int(input()), int(input())

five_en_count = N // 500

N -= (500 * five_en_count)

N -= A

print('Yes' if N <= 0 else 'No')