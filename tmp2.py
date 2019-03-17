import sys
datas = []
n = int(sys.stdin.readline().strip())
for line in range(n):
    datas.append(sys.stdin.readline().strip())
result = []
for data in datas:
    i = 0
    data = list(data)
    while i<len(data):
        if i+2<len(data):
            if data[i]==data[i+1]==data[i+2]:
                data.remove(data[i])
            else:
                i+=1
        else:
            break
    i = 0
    while i<len(data):
        if i+3<len(data):
            if data[i]==data[i+1] and data[i+2]==data[i+3]:
                data.remove(data[i+2])
            else:
                i+=1
        else:
            break
    result.append(data)
for res in result:
    print(''.join(res))
