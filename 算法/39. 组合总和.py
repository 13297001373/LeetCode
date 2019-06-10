class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(i,tmp_sum,tmp):
            if tmp_sum>target or i==n:
                return
            if tmp_sum == target:
                res.append(tmp)
                return
            backtrack(i,tmp_sum+candidates[i],tmp+[candidates[i]]) ##需要candidates[i]
            backtrack(i+1,tmp_sum,tmp) ##不需要candidates[i]
        n = len(candidates)
        res = []
        backtrack(0,0,[])
        return res
def test_function():
     solution = Solution()
     candidates = [2,3,6,7]
     target = 7
     res = solution.combinationSum(candidates,target)
     print(res)

if __name__ == '__main__':
    test_function()