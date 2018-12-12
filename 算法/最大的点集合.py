n = int(input())
dicts = {}
while n>0:
    row = input()
    row = [int(i) for i in row.split(' ')]
    dicts[row[0]] = row[1]
    n-=1
maxs = []
keys = sorted(dicts.items(),key=lambda x:x[0],reverse=True)
length = len(keys)
max_y = keys[0][1]
for i in range(length):
    if keys[i][1]>=max_y:
        max_y = keys[i][1]
        maxs.append(keys[i])
for point in maxs[::-1]:
    print(point[0],point[1])
