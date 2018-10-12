# coding=utf-8
#三类小球，同色不相邻问题
#(m,n,k)=(m-1,n,k)*(n+k-m+2)+(m-1,n-1,k)nA2+(m-1,n,k-1)kA2 且(1,1,1)=3!

#冒泡排序从大到小排列
def rank(num):
    for j in range(len(num)):
        for i in range(len(num)-1):
            if num[i]<num[i+1]:
                a=num[i]
                num[i]=num[i+1]
                num[i+1]=a
    return(num)


#递归计算 (m,n,k)=(m-1,n,k)*(n+k-m+2)+(m-1,n-1,k)nA2+(m-1,n,k-1)kA2 且(1,1,1)=3!
def start(m,n,k):
    num=[m,n,k]
    num=rank(num)

    #(1,1,1)时候为3！
    if num[2]==1 and num[1]==1 and num[0]==1:
        N=factorial(3)
        return(N)
    else:
        # 首先(m,n,k)=(m-1,n,k)*(n+k-m+2)是肯定有的递归
        N=start(num[0]-1,num[1],num[2])*(num[1]+num[2]-num[0]+2)
        #  判断其它两个是否大于2,大于2就需要计算(m-1,n-1,k)nA2和(m-1,n,k-1)kA2
        if num[1]>=2:
            N=N+start(num[0]-1,num[1]-1,num[2])*(num[1]*(num[1]-1))
        if num[2]>=2:
            N=N+start(num[0]-1,num[1],num[2]-1)*(num[2]*(num[2]-1))
        #print(N)
        return(N)


#递归计算阶乘
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n*factorial(n-1))


#-----------------------------备忘录算法---------------------------
def mstart(m, n, k):
    num = [m, n, k]
    num = rank(num)
    # (1,1,1)时候为3！
    if num[2] == 1 and num[1] == 1 and num[0] == 1:
        N = factorial(3)
        return (N)
    else:
            # 首先(m,n,k)=(m-1,n,k)*(n+k-m+2)是肯定有的递归
        N = map(num[0] - 1, num[1], num[2]) * (num[1] + num[2] - num[0] + 2)
            #  判断其它两个是否大于2,大于2就需要计算(m-1,n-1,k)nA2和(m-1,n,k-1)kA2
        if num[1] >= 2:
            N = N + map(num[0] - 1, num[1] - 1, num[2]) * (num[1] * (num[1] - 1))
        if num[2] >= 2:
            N = N + map(num[0] - 1, num[1], num[2] - 1) * (num[2] * (num[2] - 1))
            # print(N)
        return (N)
def map(m,n,k):
    if (str(m)+str(n)+str(k)) in Memorandum:
        return Memorandum.get((str(m)+str(n)+str(k)))
    else:
        Memorandum[(str(m)+str(n)+str(k))]=mstart(int(m),int(n),int(k))
        return Memorandum.get((str(m)+str(n)+str(k)))


if __name__=='__main__':
    num=[]
    Memorandum={}
    for i in range(3):
        n=input("输入第"+str(i+1)+"类小球数量")
        num.append(int(n))
    #print(num)
    #此为区分同类小球的排列数目 mstart使用备忘录算法，时间复杂度降低，start是普通递归
    M=mstart(num[0],num[1],num[2])

    print(M)
    #若不区分同类小球，需要除以(mAm*nAn*kAk)即(m!n!k!)
    P=M/(factorial(num[0])*factorial(num[1])*factorial(num[2]))
    print(P)