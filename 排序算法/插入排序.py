'''
插入排序：时间复杂度为n**2,稳定，best：n worst：n**2，space：1
'''
def Insert_sort(nums):
    for i in range(1,len(nums)):
        x = nums[i]
        j = i-1
        while j>=0:
            if nums[j]>x:
                nums[j+1] = nums[j]
                nums[j] = x
                j-=1
            else:
                break
    return nums

if __name__ == '__main__':
    Arr = [1, 3, 9, 2, 4, 2, 4, 6, 7]
    print(Insert_sort(Arr))
