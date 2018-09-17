class UF(object):
    def __init__(self,grid):
        self.size = len(grid)*len(grid[0])+1
        self.id = [i for i in range(self.size)]
        self.rank = [0 for _ in range(self.size)]

    def find(self,p):
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p

    def connected(self,p,q):
        return self.find(p) == self.find(q)

    def connect(self,p,q):
        i = self.find(p)
        j = self.find(q)
        if i==j:return
        if self.rank[i]<self.rank[j]:
            self.id[i] = j
        else:
            self.id[j] = i
            if self.rank[i] ==self.rank[j]:
                self.rank[i]+=1


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:return 0
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    self.dfs(grid,m,n,i,j)
                    count+=1
        return count

    def dfs(self,grid,m,n,i,j):
        if i<0 or i>=m or j<0 or j>=n or grid[i][j]=='0':return
        grid[i][j]='0'
        self.dfs(grid,m,n,i+1,j)
        self.dfs(grid,m,n,i-1,j)
        self.dfs(grid,m,n,i,j+1)
        self.dfs(grid,m,n,i,j-1)


if __name__ == '__main__':
    s = Solution()
    grid = [['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']]
    res = s.numIslands(grid)
    print(res)