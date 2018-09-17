class UF(object):
    def __init__(self,board):
        self.size = len(board) * len(board[0]) + 1
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
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:return
        uf = UF(board)
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if (i==0 or i==m-1 or j==0 or j==n-1) and board[i][j]=='O':
                    uf.connect(i*n+j,m*n)
                elif board[i][j]=='O':
                    if board[i-1][j]=='O':
                        uf.connect((i-1)*n+j,i*n+j)
                    if board[i+1][j]=='O':
                        uf.connect((i + 1) * n + j, i * n + j)
                    if board[i][j-1]=='O':
                        uf.connect(i * n + j-1, i * n + j)
                    if board[i][j+1]=='O':
                        uf.connect(i * n + j + 1, i * n + j)
        for i in range(m):
            for j in range(n):
                if not uf.connected(i*n+j,m*n):
                    board[i][j]='X'
        return board

if __name__ == '__main__':
    s = Solution()

    board = [
                ['X', 'X', 'X', 'X'],
                ['X', 'O', 'O', 'X'],
                ['X', 'X', 'O', 'X'],
                ['X', 'O', 'X', 'X']
            ]
    # board = [["X", "O", "X", "X"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"],
    #  ["O", "X", "O", "X"]]
    res = s.solve(board)
    print(res)