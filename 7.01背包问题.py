#小偷有一个容量为W的背包，有n件物品，第i个物品价值vi，且重wi
#目标: 找到xi使得对于所有的xi = {0, 1}
#sum(wi*xi) <= W, 并且sum(xi*vi)最大

# #递归解法
# class solution:
#     def __init__(self):
#         self.f={} #字典形式的备忘录，可以用列表
#     def search(self,n,W,v,w):
#         if str(n)+str(W) in self.f:
#             return self.f.get(str(n)+str(W))
#         a=0
#         if n<0:
#             return 0
#         if W>=w[n]:
#             a=self.search(n-1,W-w[n],v,w)+v[n] #第n件物品装进背包
#         b=self.search(n-1,W,v,w) #第n件物品不装进背包
#
#         self.f[str(n)+str(W)]=max(a,b) #前n件最大价值
#         return self.f[str(n)+str(W)]
#
# if __name__=='__main__':
#     A=solution()
#     B=A.search(3,30,[3,4,5,7],[10,20,20,30])  #n=3,其实有4个值
#     print(B)
# #    for i in A.f:
# #        print(i,A.f[i])
#
#
# #leetcode 416 分组问题,能否分成和相等的两组
# #Input: [1, 5, 11, 5]
# #Output: true
# #Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         return self.bag(0,0,nums)
#
#
#     def bag(self,lsum,rsum,nums):
#         if lsum==rsum and len(nums)==0:
#             return True
#         if len(nums)>0:
#             a=self.bag(lsum+nums[len(nums)-1],rsum,nums[:len(nums)-1])
#             b=self.bag(lsum,rsum+nums[len(nums)-1],nums[:len(nums)-1])
#             if a==True or b==True:
#                 return True
#
#         return False


# 01背包正向解法
def bag(n,c,w,v):
    '''
    n 物品的数量
    c 书包能承受的重量
    w 每个物品的重量
    v 每个物品的价值
    '''

    value= [[0 for j in range(c+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,c+1):
            value[i][j]=value[i-1][j]
            #背包放得下，但是
            if j>w[i-1] and value[i][j]<value[i-1][j-w[i-1]]+v[i-1]:
                value[i][j] = value[i-1][j-w[i-1]]+v[i-1]
    return value

def show(n,c,w,value):
    '''
    n 物品的数量
    c 书包能承受的重量
    w 每个物品的重量
    value 正向矩阵
    '''
    print("最大值为：",value[n][c])
    x = [False for i in range(n)]
    j = c
    for i in range(n,0,-1):
        if value[i][j]>value[i][j-1]:
            x[i-1] = True
            j -= w[i-1]
    for i in range(n):
        if x[i]:
            print('第',i+1,'个',end='')




