class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(i,tmp_num,tmp):
            if tmp_num==target:
                tmp = sorted(tmp)
                if tmp not in res:
                    res.append(tmp)
                    return
                return
            if i==n or tmp_num>target:
                return
            backtrack(i+1,tmp_num+candidates[i],tmp+[candidates[i]])
            backtrack(i+1,tmp_num,tmp)
        n = len(candidates)
        res= []
        backtrack(0,0,[])
        return res

def test_function():
    solution =Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    res = solution.combinationSum2(candidates,target)
    print(res)

if __name__ == '__main__':
    test_function()