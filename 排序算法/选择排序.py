'''
选择排序：时间复杂度为n**2,不稳定，best：n**2 worst：n**2，space：1
'''
def Selection_Sort(Arr):
    length = len(Arr)
    for i in range(1,length):
        max = Arr[0]
        for j in range(1,length-i+1):
            if max<Arr[j]:
                max = Arr[j]
                index = j
        tmp = Arr[index]
        Arr[index] = Arr[-i]
        Arr[-i] = tmp
    return Arr

if __name__ == '__main__':
    Arr = [1,3,9,2,4,2,4,6,7]
    print(Selection_Sort(Arr))
