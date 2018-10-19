#coding=utf-8

def Quicksort(data,low,high):
    if high>low:
        #传入参数，通过partitions函数，获取k下标值
        k = Partitions(data,low,high)
        #递归排序列表k下标左侧的列表
        Quicksort(data,low,k-1)
        #递归排序列表k下标右侧的列表
        Quicksort(data,k+1,high)

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
        while mylist[right] >= base and left < right:
            right = right - 1
        mylist[left]=mylist[right]
        #当left对应的值小于参考值，就一直向右移动
        while mylist[left] <= base and left < right:
            left += 1
        mylist[right]=mylist[left]

    #若移动完，已经相遇，则交换right对应的值和参考值
    mylist[left] = base
    #返回left===right值
    return right


#三行代码快速排序
def qsort(L):
    if len(L) <= 1: return L
    return qsort([lt for lt in L[1:] if lt < L[0]]) + L[0:1]+ \
    qsort([ge for ge in L[1:] if ge >= L[0]])

list_demo = [2,3,4,5,1,6,7,8,9,10]
print(list_demo)
q=qsort(list_demo)
print(q)



p=GetLeastNumber(list_demo,0,9,3)
print(p)

Quicksort(list_demo,0,9)
print(list_demo)