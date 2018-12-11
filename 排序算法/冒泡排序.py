'''
冒泡排序：时间复杂度为n**2,稳定，best：n worst：n**2，space：1
'''
def Bubble_Sort(Arr):
    length = len(Arr)
    for i in range(1,length): ##轮次n-1
        for j in range(0,length-i):
            if Arr[j]>Arr[j+1]:
                tmp = Arr[j]
                Arr[j] = Arr[j+1]
                Arr[j+1] = tmp
    return Arr
if __name__ == '__main__':
    Arr = [1,3,9,2,4,2,4,6,7]
    print(Bubble_Sort(Arr))

