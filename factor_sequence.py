#coding=utf-8
#有多少 长度为n的整数序列A1到An，满足An=M，1<Ai<M且Ai能整除Ai+1(1<=i<N)
#例如 n=3,An=3, 有113,133,333,三种

#计算因子
import time

def allFactor(n):
    if n==0:return([0])
    if n==1:return([1])
    rlist=[]
    i=1
    while i<=n:
        if n%i ==0:
            rlist.append(i)

        i +=1
    return rlist

#递归，返回计算数
def factornumber(a,n):
    all=0
    #这里只做求因子函数的备忘录
    b=mapping1(a)
    #b=allFactor(a)
    m=len(b)
    #print(m)
    if n==1:
        return(1)
    if n==2:
        return(m)
    else:
        for i in range(m):
            #递归传入两个参数，要用备忘录算法递归程序要重新写。
            all=all+factornumber(b[i],n-1)
        return all

#备忘录
def mapping1(n):
    if n in Memorandum1:
        return Memorandum1.get(n)
    else:
        Memorandum1[n] = allFactor(n)
        return Memorandum1.get(n)



if __name__ == '__main__':
    start=time.clock()
    print(allFactor(1000))
    Memorandum1={}
    q=factornumber(24,3)
    print(q)
    print(Memorandum1)
    end=time.clock()
    print('Running time: %s Seconds' % (end - start))