n = int(input())
members = []
result = []

for i in range(n):
    weight, height = map(int, input().split())
    members.append([weight, height])

for idx in range(len(members)):
    ranking = 1
    for member in members:
        if members[idx] == member:
            continue
        else:
            if members[idx][0] < member[0] and members[idx][1] < member[1]:
                ranking += 1
    result.append(str(ranking))

print(' '.join(result))