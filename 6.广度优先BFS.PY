#leetcode 200
#给一个二维网格，1代表陆地，0代表海洋，问你这个网格中有多少个岛，边界以外的为海洋
#Input:
#11110
#11010
#11000
#00000
#Output: 1

#遍历网格grid，另外建立一个g，判断是否搜素过。

class Solution:
    def __init__(self):
        self.Q=[]
    
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid=grid
        self.n=len(self.grid)
        if self.n==0:
            return 0
        self.m=len(self.grid[0])
        #g表示是否访问过
        self.g = [ [0]*self.m for i in range(self.n)]
        
        ans=0
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j]=='1' and self.g[i][j]==0:  #必须是陆地且未被访问过 
                    self.floodfill(i,j)     #判断上下左右
                    ans +=1
        #print(self.g)
        return ans 
    
    #广度优先搜索
    def floodfill(self,a,b):
        self.Q.append([a,b])  #??
        self.g[a][b]==1 
        while len(self.Q)>0:
            [x,y]=self.Q.pop(0)
            x1,y1=x-1,y
            x2,y2=x,y-1
            x3,y3=x+1,y
            x4,y4=x,y+1
            if x1>=0 and y1>=0 and x1<self.n and y1<self.m and self.g[x1][y1]==0 and self.grid[x1][y1]=='1':   #属于同一个岛
                self.g[x1][y1]=1 
                self.Q.append([x1,y1])
            if x2>=0 and y2>=0 and x2<self.n and y2<self.m and self.g[x2][y2]==0 and self.grid[x2][y2]=='1':   #属于同一个岛
                self.g[x2][y2]=1 
                self.Q.append([x2,y2])
            if x3>=0 and y3>=0 and x3<self.n and y3<self.m and self.g[x3][y3]==0 and self.grid[x3][y3]=='1':   #属于同一个岛
                self.g[x3][y3]=1 
                self.Q.append([x3,y3])
            if x4>=0 and y4>=0 and x4<self.n and y4<self.m and self.g[x4][y4]==0 and self.grid[x4][y4]=='1':   #属于同一个岛
                self.g[x4][y4]=1 
                self.Q.append([x4,y4])
            #print(self.Q)
