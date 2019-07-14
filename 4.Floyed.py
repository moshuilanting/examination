#leetcode 399. Evaluate Division

# Given a / b = 2.0, b / c = 3.0. 
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        N=[]
        for i in range(len(equations)):
            for j in range(2):
                if equations[i][j] not in N:
                    N.append(equations[i][j])
        N_long=len(N)
            
        N_matrix = [[21472147]*N_long for i in range(N_long)]
        for i in range(len(equations)):
            N_matrix[N.index(equations[i][0])][N.index(equations[i][1])]=values[i]
            N_matrix[N.index(equations[i][1])][N.index(equations[i][0])]=1/values[i]
        for i in range(N_long):
            N_matrix[i][i]=1
            
        #print(N_matrix)
                
        d=[ [21472147]*N_long for i in range(N_long)] #d用于存放任意两点间的距离

        #三重循环，把距离矩阵都求出来了
        for k in range(N_long):
            for i in range(N_long):
                for j in range(N_long):
                    #题目要求，这里是*不是常见的+
                    N_matrix[i][j]=min(N_matrix[i][j],N_matrix[i][k]*N_matrix[k][j])
                    
        d=[]
        for i in range(len(queries)):
            if queries[i][0] in N and queries[i][1] in N:
                A=N.index(queries[i][0])
                B=N.index(queries[i][1])
                if N_matrix[A][B] < 1000: #阈值得设啊，因为初始化值21472147并不等于无穷大。
                    d.append(N_matrix[A][B])
                else:
                    d.append(-1)
            else:
                d.append(-1)
        return d
