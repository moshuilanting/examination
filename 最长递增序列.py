#leetcode 300
#input [10,9,2,5,3,7,101,18]
#output 4


#纯动态规划 n*2
#[10,9,2,5,3,7,101,18]
#[1 ,1,1,2,2,3, 4,  4] #10最多只能为1个最长序列，5可以由[2,5]构成2个最长序列

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        d=[1]*len(nums)
        for i in range(len(nums)):
            for j in range(i+1):
                if nums[i]>nums[j]:
                    d[i]=max(d[j]+1,d[i])
        return max(d)

'''
#动态规划加二分查找 nlon(n)
找到一个数，若大于数组中所有数，则加在后面，若小于,替换掉刚好大于的那个数。
这样做求出整个序列会错，但是长度一样。
[10]
[9]
[2]
[2,5]
[2,3]
[2,3,7]
[2,3,7,101]
[2,3,7,18]
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        d=[nums[0]]
        for i in range(1,len(nums)):
            n=self.binarysearch(d,nums[i],0,len(d)-1)
            if n<len(d):
                d[n]=nums[i]
            else:
                d.append(nums[i])
        return len(d)

    #二分查找，查到了输出查到那个数的地址，没查到返回low（此时low>high）,查找最相近的大数。
    def binarysearch(self,seq, v, low, high):
        while low <= high:
            mid = (low + high) // 2
            if v == seq[mid]:
                return mid
            elif v > seq[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return low


#最长重复序列
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp=[[0]*len(A) for i in range(len(B))]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i]==B[j]:
                    if i==0 or j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j]=dp[i-1][j-1]+1
        return max(max(row) for row in dp)
