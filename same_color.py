# coding=utf-8
#三类小球，同色不相邻问题
#class same_color():
def rank(num):

    for j in range(len(num)):
        for i in range(len(num)-1):
            if num[i]<num[i+1]:
                a=num[i]
                num[i]=num[i+1]
                num[i+1]=a

    return(num)



def start(m,n,k):
    num=[m,n,k]
    num=rank(num)
    #print(num)


    if num[2]==1 and num[1]==1 and num[0]==1:
        N=factorial(3)
        #print(N)
        return(N)
    else:
        N=start(num[0]-1,num[1],num[2])*(num[1]+num[2]-num[0]+2)
        if num[1]>=2:
            N=N+start(num[0]-1,num[1]-1,num[2])*(num[1]*(num[1]-1))
        if num[2]>=2:
            N=N+start(num[0]-1,num[1],num[2]-1)*(num[2]*(num[2]-1))
        #print(N)
        return(N)



def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n*factorial(n-1))




if __name__=='__main__':
    n=input("输入种类")
    num=[]
    for i in range(int(n)):
        num.append(int(input()))
    #print(num)

    M=start(num[0],num[1],num[2])
    print(M)
    P=M/(factorial(num[0])*factorial(num[1])*factorial(num[2]))
    print(P)