# def f(n1, n2):
#     ss = 0
#     aa = False
#     cc = 0
#     for i in range(len(n1)):
#         if not n1[i][1] and not n2[i][1]:
#             if n1[i][0] == n2[i][0]:
#                 ss += 1
#                 aa = True
#             else:
#                 aa = False
#             if aa:
#                 cc += 1
#         else:
#             aa = False
#
#     return ss + cc ** 2
#
#
# def solution(answer_sheet, sheets):
#     answer = -1
#     lst = dict()
#     for i in range(len(sheets)):
#         lst[i] = []
#     for j, sheet in enumerate(sheets):
#         for i in range(len(answer_sheet)):
#             if sheet[i] == answer_sheet[i]:
#                 lst[j] += [[sheet[i], True]]
#             else:
#                 lst[j] += [[sheet[i], False]]
#
#     for i in range(len(lst)):
#         for j in range(i+1, len(lst)):
#             suspect = f(lst[i], lst[j])
#
#
#     return lst


# def get_len(road):
#     count = 0
#     x = 0
#     if road.count("0") == 0:
#         return len(road)
#
#     for ch in road:
#         if ch == "1":
#             x += 1
#         else:
#             if x > count:
#                 count = x
#             x = 0
#     if x > count:
#         count = x
#
#     return count
#
#
# def f(road, n, lst):
#     x = 0
#     i = 0
#     dummy_road = road.copy()
#     while n > 0 and i < len(lst):
#         idx = lst[i]
#         dummy_road[idx] = "1"
#         n -= 1
#         i += 1
#     return get_len(dummy_road)
#
#
# def solution1(road, n):
#     road = list(road)
#     lst = []
#     s = []
#     for i in range(len(road)):
#         if road[i] == '0':
#             lst.append(i)
#     while lst:
#         length = f(road, n, lst)
#         s.append(length)
#         lst.pop(0)
#
#     return max(s)

def split_slash(ch):
    return ch.split('/')[1:]


def solution(directory, command):
    for ch in command:
        try:
            comm, direc = ch.split()
        except ValueError:
            comm, old, new = ch.split()
        if comm == 'mkdir':
            directory.append(direc)
        elif comm == 'rm':
            s = split_slash(direc)[-1]
            i = 0
            while i < len(directory):
                if directory[i].find(s) != -1:
                    directory.pop(i)
                i += 1
        # elif comm == 'cp':
    answer = sorted(directory, reverse=True)
    answer.insert(0, answer.pop(-1))
    return sorted(directory)
#
# a = "4132315142"
# s = ["3241523133","4121314445","3243523133","4433325251","2412313253"]
# # print(solution(a, s))
# print(solution1("001100", 5))
# '/hello/tmp'.find('ro')
# print('/hello/tmp'.startswith('/'+'hello'))
# print('/hello/tmp'.find('ro'))

s = [
"/",
"/hello",
"/hello/tmp",
"/root",
"/root/abcd",
"/root/abcd/etc",
"/root/abcd/hello"
]
c = [
"mkdir /root/tmp",
"cp /hello /root/tmp",
"rm /hello"
]
print(solution(s, c))