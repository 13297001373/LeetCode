s = "let's it go"
res = s.split()
print(res)
for item in res:
    print(''.join(list(item)[::-1]))
print(res)