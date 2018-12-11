class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        length = []
        for row in strs:
            length.append(len(row))
        for i in range(min(length)):
            for j in range(len(strs)-1):
                if strs[j][i] != strs[j+1][i]:
                    return strs[0][:i]
        return strs[0][:min(length)]
if __name__ == '__main__':
    solutin = Solution()
    strs = ["flower","flow","flight"]
    result = solutin.longestCommonPrefix(strs)
    print(result)
