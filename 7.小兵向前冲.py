class solution:
    def go(self,n,m):
        #for i in range(n):
            #for j in range(m):
        if n*m>0:
            return self.go(n-1,m)+self.go(n,m-1)
        else:
            return 1

if __name__=='__main__':
    A=solution()
    print(A.go(100,100)) #2*2的棋盘，输入1*1
