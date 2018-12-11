class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        counts = 0
        hash = dict()
        for c in C:
            for d in D:
                if c+d in hash.keys():
                    hash[c+d]+=1
                else:
                    hash[c+d] = 1
        for a in A:
            for b in B:
                if -(a+b) in hash.keys():
                    counts+=hash[-(a+b)]
        return counts

if __name__ == '__main__':
    solution = Solution()
    A=[1, 2]
    B=[-2, -1]
    C=[-1, 2]
    D=[0, 2]
    solution.fourSumCount(A,B,C,D)