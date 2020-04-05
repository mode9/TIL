def my_answer():
    n = int(input())
    count = 0
    i = 666
    result = ''
    while n != count:
        result = str(i)
        if '666' in result:
            count += 1
        i += 1
    print(result)


def better_solution():
    N = int(input())
    if N == 1:
        print(666)
    else:
        count = 1
        for i in range(2, N + 1):
            base_title = "{0}666".format(i - 1)
            num_of_extra_six_in_row = 0
            for k in range(len(base_title) - 3):
                if base_title[-4 - k] == '6':
                    num_of_extra_six_in_row += 1
                else:
                    break
            count += int(10 ** num_of_extra_six_in_row)
            if count >= N:
                break

        if num_of_extra_six_in_row > 0:
            base = int(10 ** num_of_extra_six_in_row)
            count -= base
            base_title = int(base_title) - int(base_title) % base + (N - count - 1)

        print(base_title)
