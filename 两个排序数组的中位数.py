class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1 = len(nums1)
        n2 = len(nums2)
        i = j =0
        list = []
        while i <n1 and j<n2:
            if nums1[i]<nums2[j]:
                list.append(nums1[i])
                i+=1
            else:
                list.append(nums2[j])
                j+=1
        if i == n1:
            for k in range(j,n2):
                list.append(nums2[k])
        if j == n2:
            for k in range(i,n1):
                list.append(nums1[k])
        n = len(list)
        if n%2 ==0:
            index = n//2
            return (list[index]+list[index-1])/2
        else:
            index = n//2
            return list[index]

if __name__ == '__main__':
    nums1 = [1,2]
    nums2 = [-1,3]
    solution = Solution()
    center = solution.findMedianSortedArrays(nums1,nums2)
    print(center)