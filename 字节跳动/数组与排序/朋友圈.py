class Solution(object): #BFS
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        count = 0
        visited = [0 for i in range(n)]
        for i in range(n):
            if not visited[i]:
                count+=1
                self.bfs(M,visited,i)
        return count
    def bfs(self,M,visited,i):
        quee = []
        visited[i] = 1
        quee.append(i)
        while len(quee)>0:
            node = quee.pop(0)
            for j in range(len(M)):
                if not visited[j] and M[node][j]:
                    quee.append(j)
                    visited[j] = 1
def test_fucntion():
    solution = Solution()
    M = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    result = solution.findCircleNum(M)
    print(result)

if __name__ == '__main__':
    test_fucntion()

