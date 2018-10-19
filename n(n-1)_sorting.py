#coding=utf-8
#2018年bilibili 校招
# 孙悟空收了n个徒弟,每个徒弟都有战斗力,徒弟可以两两组合相乘( n(n-1)/2 种情况)，组合徒弟中战斗力排名第k的组合徒弟战斗力
# 例如输入：
#5 2             5是五个徒弟，2是求排名第2的组合徒弟战斗力
#1 3 4 5 9
#输出：
#36

#三行代码快速排序
def qsort(L):
    if len(L) <= 1: return L
    left=qsort([ge for ge in L[1:] if ge >= L[0]])
    light=qsort([lt for lt in L[1:] if lt < L[0]])
    return  left + L[0:1]+ light

#求数组data的[start,end]中最小的k个数
def GetLeastNumber(data,start,end,k):
    index=Partitions(data,start,end)

    while(index!=k-1):
        if(index>k-1):
            end=index-1
            index=Partitions(data,start,end)
        else:
            start=index+1
            index=Partitions(data,start,end)

    return data[:k]


def Partitions(mylist,low,high):
    left = low
    right = high
    #将最左侧的值赋值给参考值base,所以要从右侧向左移动先开始
    base = mylist[left]
    #当left下标，小于right下标的情况下，此时判断二者移动是否相交，若未相交，则一直循环
    #mylist[right] <= base and mylist[left] >= base and left < right 则从大到小排序
    while left < right :
        # 当right对应的值大于参考值，就一直向左移动,
        while mylist[right] <= base and left < right:
            right = right - 1
        mylist[left]=mylist[right]
        #当left对应的值小于参考值，就一直向右移动
        while mylist[left] >= base and left < right:
            left += 1
        mylist[right]=mylist[left]

    #若移动完，已经相遇，则交换right对应的值和参考值
    mylist[left] = base
    #返回left===right值
    return right


if __name__ == '__main__':
    n, k = map(int, input().split())
    tudi= list(map(int, input().split()))
    tudi=tudi[:n]
    Ability=[]


    
    for i in tudi:
        a=list(map(lambda x:x*i,tudi))
        Ability.append(a)
    for i in range(n):
        del Ability[i][i]

    y=[]
    for i in range(n-1):
        for j in range(n-1):
                y.append(Ability[i][j])
    print(y)
    L=GetLeastNumber(y,0,len(y)-1,k)
    L=qsort(L)
    print(L)

