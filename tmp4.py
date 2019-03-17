import sys
a = input()
result = list(map(int,a.split()))
lines = list(map(float,input().split()))
i = 1
if result[1]<=result[0]:
    print(min(lines))


