'''
给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
'''
class Solution:
    def removerDuplicates(self,nums):
        '''
        :param nums: list[int]
        :return: int
        '''
        i = 0
        while i<len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.remove(nums[i+1])
            else:
                i+=1
        return len(nums)

if __name__ == '__main__':
    nums = [1,1,2]
    s = Solution()
    length = s.removerDuplicates(nums)
    print(length)
    print(nums)

'''
#remove删除首个符合条件的元素，并不删除特定的索引。
n =[1,2,2,3,4,5]
n.remove(3)
print (n)
#输出  [1, 2, 2, 4, 5]
####----------------#######################
#pop按照索引删除字符，返回值可以付给其他的变量，返回的是你弹出的那个数值。
n =[1,2,2,3,4,5]
a=n.pop(4)
print (a)
print (n)
#输出  
4
[1, 2, 2, 3, 5]
#####--------#####
#del按照索引删除字符，返回值不可以付给其他的变量。
n =[1,2,2,3,4,5]
del(n[3])
print (n)

#输出  
[1, 2, 2, 4, 5]

'''