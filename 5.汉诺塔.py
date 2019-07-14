

#递归f(n)=2*f(n-1)+1
def f(n):
    if n==1:
        return 1
    else:
        return 2*f(n-1)+1

def fanan(n,A,B,C):
    if n==0:
        return
    fanan(n-1,A,C,B)

    #全局变量N，在递归中计数，计算递归次数，即汉诺塔需要的最少步骤
    global N
    N=N+1

    print( '%d' %n +'号盘子从'+A+'中通过'+B+'放到'+C+'上.',N )
    #print('%d'+'号盘子从'+A+'中通过'+B+'放到'+C+'上.' %n)
    fanan(n-1,B,A,C)
    




if __name__ == '__main__':
    #num = f(2)
    #print(num)
    
    N=0
    fanan(6,'A','B','C')
    print(N)
    
