from pprint import pprint

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        a =[]
        for i in range(numRows):
            path =[]
            for j in range(i+1):
                if j==0 or j==i:path.append(1)
                else:path.append(a[i-1][j-1]+a[i-1][j])
            a.append(path)
        return a

    def getRow(self, rowIndex):
        a=[]
        i =0
        while True:
            path =[]
            for j in range(i+1):
                if j==0 or j==i:path.append(1)
                else:path.append(a[j-1]+a[j])
            a =path
            if i ==rowIndex:return path
            i+=1

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        a=[0 for i in range(len(triangle)+1)]
        i = len(triangle) - 1
        while i >= 0:
            for j in range(len(triangle[i])):
                a[j]=min(a[j], a[j + 1]) + triangle[i][j]
            i -= 1
        return a[0]

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        a = [[0 for i in range(n)] for j in range(m)]
        x = m - 1
        while x >= 0:
            y = n - 1
            while y >= 0:
                if x == m - 1 or y == n - 1:
                    a[x][y] = 1
                else:
                    a[x][y] = a[x][y + 1]+a[x+1][y]
                y -= 1
            x -= 1
        return a[0][0]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return None
        m, n = len(grid), len(grid[0])
        bp = [[1 for i in range(n+1)] for j in range(m+1)]
        x=m-1
        while x>=0:
            y=n-1
            while y>=0:
                if x==m-1:mi = bp[x][y+1]
                elif y==n-1:mi = bp[x+1][y]
                else:mi=min(bp[x+1][y],bp[x][y+1])
                if grid[x][y]<=0:bp[x][y]=-grid[x][y]+mi
                elif mi-grid[x][y]>=1:bp[x][y]=mi-grid[x][y]
                else:bp[x][y]=1
                y-=1
            x-=1
        return bp[0][0]

    def minDistance1(self, word1, word2):
        l1, l2 = len(word1) + 1, len(word2) + 1
        dp = [[0 for _ in range(l2)] for _ in range(l1)]
        for i in range(l1):dp[i][0] = i
        for j in range(l2):dp[0][j] = j
        for i in range(1, l1):
            for j in range(1, l2):dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (word1[i - 1] != word2[j - 1]))
        pprint(dp)
        return dp[-1][-1]

    def minDistance(self, word1, word2):
        p1, p2 = 0, 0
        return self.calculateDistance(word1, word2, p1, p2)

    def calculateDistance(self, word1, word2, p1, p2):
        if p1 >= len(word1):
            if p2>=len(word2):return 0
            else:return len(word2) - p2
        if p2 >= len(word2):
            if p1>=len(word1):return 0
            else:return len(word1) - p1
        if word1[p1] == word2[p2]:
            return self.calculateDistance(word1, word2, p1 + 1, p2 + 1)
        else:
            d1 = self.calculateDistance(word1, word2, p1, p2 + 1)
            d2 = self.calculateDistance(word1, word2, p1 + 1, p2)
            d3 = self.calculateDistance(word1, word2, p1 + 1, p2 + 1)
            return 1 + min(d1, d2, d3)
        return 0

if __name__ =="__main__":
    sol = Solution()
    # res = sol.minimumTotal([[-1],[2,3],[1,-1,-3]])
    # pprint(res)
    # res = sol.uniquePaths(2,2)
    # grid =  [[-2,-3,3],
    #         [-5,-10,1],
    #         [10,30,-5]]
    # grid = [[-3,5]]
    # res = sol.minPathSum(grid)
    # res = sol.minDistance1("jason", "json")
    res = sol.minDistance("dinitrophenylhydrazine","acetylphenylhydrazine")
    print(res)