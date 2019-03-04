##快速排序、冒泡排序、归并排序
class Sort:
    def Quicksort(self,nums,start,end):
        if  start<end:
            i = start
            j = end
            x = nums[start]
            while i<j:
                while i<j and nums[j]>x:
                    j-=1
                if i<j:
                    nums[i] = nums[j]
                    i+=1
                while i<j and nums[i]<x:
                    i+=1
                if i<j:
                    nums[j] = nums[i]
                    j-=1
            nums[i] = x
            self.Quicksort(nums,start,i-1)
            self.Quicksort(nums,i+1,end)

    def BubbleSort(self,nums):
        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]

    def MergeSort(self,nums):
        if len(nums)<=1:
            return nums
        mid = len(nums)//2
        left = self.MergeSort(nums[:mid])
        right = self.MergeSort(nums[mid:])
        return self.Merge(left,right)
    def Merge(self,left,right):
        i = 0
        j = 0
        result = []
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        result+=left[i:]
        result+=right[j:]
        return result

def test_function():
    sort = Sort()
    nums = [1,2,4,6,21,9,10,3,3]
    sort.Quicksort(nums,0,len(nums)-1)
    print("The result of QuickSort is :",nums)

    nums = [1, 2, 4, 6, 21, 9, 10, 3,3]
    sort.BubbleSort(nums)
    print("The result of BuffleSort is:",nums)

    nums = [1, 2, 4, 6, 21, 9, 10, 3,3]
    nums = sort.MergeSort(nums)
    print("The result of MergeSort is :",nums)
if __name__ == '__main__':
    test_function()