n = int(input())
loss = 1024-n
result = [0,0,0,0]
result[0] = loss//64
result[1] = (loss-64*result[0])//16
result[2] = (loss-64*result[0]-16*result[1])//4
result[3] = (loss-64*result[0]-16*result[1]-4*result[2])
print(sum(result))
