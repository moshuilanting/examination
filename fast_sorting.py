#coding=utf-8

def Quicksort(list,low,high):
    if high>low:
        #传入参数，通过partitions函数，获取k下标值
        k = Partitions(list,low,high)
        #递归排序列表k下标左侧的列表
        Quicksort(list,low,k-1)
        #递归排序列表k下标右侧的列表
        Quicksort(list,k+1,high)

def Partitions(list,low,high):
    #以第一数为基准，从第二个数开始比较
    left = low+1
    right = high
    #将最左侧的值赋值给参考值k
    k= list[low]
    #当left下标，小于right下标的情况下，此时判断二者移动是否相交，若未相交，则一直循环
    while(left<right):
        #当left对应的值小于k参考值，就一直向右移动
        while(list[left]<k):
            left += 1
        while(list[right]>=k):
            right -= 1
        if left<right:
            list[left],list[right]=list[right],list[left]
    #若移动完，已经相遇，则交换right对应等值和参考值
    list[low] = list[right]
    list[right] = k
    #返回k值
    return right


#三行代码快速排序
def qsort(L):
    if len(L) <= 1: return L

    return qsort([lt for lt in L[1:] if lt < L[0]]) + L[0:1]+ \
    qsort([ge for ge in L[1:] if ge >= L[0]])

list_demo = [6,1,2,7,9,4,3,5,10,8]
print(list_demo)
q=qsort(list_demo)
print(q)
Quicksort(list_demo,0,9)
print(list_demo)

L=[1,2,3,4,5,6,7]
q= [i for i in L if i<4]
for i in L:
    i=i+2
print(q)
print(L)