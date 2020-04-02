def get_minimum_count(lst):
    wb_row = 'WB' * 4
    bw_row = 'BW' * 4
    w_count = 0
    b_count = 0
    w_table = [wb_row, bw_row] * 4
    b_table = [bw_row, wb_row] * 4
    for i in range(8):
        for j in range(8):
            if lst[i][j] != w_table[i][j]:
                w_count += 1
    for i in range(8):
        for j in range(8):
            if lst[i][j] != b_table[i][j]:
                b_count += 1
    return min(w_count, b_count)


n, m = map(int, input().split())
count_lst = []
arr = [input() for _ in range(n)]

for i in range(0, n - 7):
    for j in range(0, m - 7):
        table = [row[j:j + 8] for row in arr[i:i + 8]]
        count_lst += [get_minimum_count(table)]
print(min(count_lst))