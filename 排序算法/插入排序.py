'''
插入排序：时间复杂度为n**2,稳定，best：n worst：n**2，space：1
'''
def Insert_Sort(Arr):
    length = len(Arr)
    for i in range(length-1):
        tmp = Arr[i+1]
        for j in range(i,-1,-1):
            if Arr[j]>tmp:
                Arr[j+1] = Arr[j]
            else:
                Arr[j+1] = tmp
                break
    return Arr

if __name__ == '__main__':
    Arr = [1, 3, 9, 2, 4, 2, 4, 6, 7]
    print(Insert_Sort(Arr))
