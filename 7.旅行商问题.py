# 当前在n,未来可以去d[]
class solution:

    # n起始点,未来可以去d[]
    def TSP(self, n, d):
        if len(d) == 0:
            return 0
        h = 21472147
        for i in range(len(d)):
            m = d[i]  # m是要去的地方
            q = d[:]
            q.remove(m)
            a = self.TSP(m, q) + c[n][m]
            if a < h:
                h = a
        return h





# 01背包问题，怎么取最大（不仅仅只求最大值，把怎么取也求出来）保存最优的求解路径


#分治阶乘算法 10!  计算362880（9！）*10 大数 比 两个小数复杂,，这个方法在大数时有差别。
#[1,2,3,4,5,6,7,8,9,10] -> [6,14,24,36,50] ->[144,504,50] ->[72576,50]=3628800
# 2*3=6*4=24*5=120*6=720*7=5040*8=40320*9=362880*10=3628800
def factoria(N):
    if N==0:
        return 1
    N2=N
    a=list(range(1,N+1))
    while N2>1:
        N1=N2%2; N2=N2//2+N1
        for i in range(N2-N1):
            a[i]*=a[N2+i]
        a=a[0:N2]
    return a[0]

#递推求解
def do(d,n):
    if len(d)==0:
        return
    for i in range(len(d)):
        q=d[:]
        q.remove(d[i])
        #针对旅行商人问题
        for j in range(factoria(len(d)-1)):
            m[n].append(d[i])
        do(q,n+1)


if __name__ == '__main__':
     c = [[0, 3, 6, 7], [5, 0, 2, 3], [6, 4, 0, 2], [3, 7, 5, 0]]
     A = solution()
     d=[0,1,2,3]
     n=0
     d.remove(n)
     #指定开始在n
     B=A.TSP(n,d)
     print(B)

     #填表法，将求解路径保存下来
     #行：代表步数，最后一行用于计算消费。列：是有多少种情况
     m = []
     d = [0, 1, 2, 3]
     for i in range(len(d)):
         m.append([])
         print(m)
     #m=[[],[],[],[],[]]
     #递推求解
     do([0,1,2,3],0)
     for u in m:
        print(u)

     #顺序求解
     for i in range(len(m[0])):
        cost=0
        #实际步数的长度-1
        for j in range(len(m)-2 ):
            cost+=c[m[j][i]][m[j+1][i]]
        m[-1].append(cost)
     for u in m:
        print(u)




