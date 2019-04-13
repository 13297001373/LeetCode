import sys
a = sys.stdin.readline().split()
n = int(a[0])
k = int(a[1])
line = sys.stdin.readline().split()
values = list(map(int,line))
def find_min(lists):
    min_value = 999999999999
    for i in lists:
        if i>0 and i<min_value:
            min_value = i
    return min_value


while k>0:
    min_value = find_min(values)
    print(min_value)
    values = list(map(lambda x:x-min_value,values))
    k-=1
