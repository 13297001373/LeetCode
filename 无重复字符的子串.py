class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        i = 0
        list = []
        while i< len(s):
            count = 1
            j = i+1
            while j<len(s):
                tmp = s[i:j]
                if s[j] not in tmp:
                    count+=1
                    j+=1
                else:
                    break
            i+=1
            list.append(count)
        return max(list)




if __name__ == '__main__':
    solution = Solution()
    strs = 'dvdf'
    result = solution.lengthOfLongestSubstring(strs)
    print(result)