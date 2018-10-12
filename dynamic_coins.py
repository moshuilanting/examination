#coding=utf-8
#假设有几种硬币，如1、3、5，并且数量无限。请找出能够组成某个数目的找零所使用最少的硬币数。
#sum[k] = min(sum[k-coin[0]] , sum[k-coin[1]], ...)+1

import sys
'''
#递归解法
def need_coins(k):
    if k==1 or k==3 or k==5:
        return 1
    elif k==2 or k==4:
        return 2
    else:
        return(min(need_coins(k-1),need_coins(k-3),need_coins(k-5))+1)


if __name__=='__main__':
    number=input("需要的零钱：")
    n = need_coins(int(number))
    print(n)
'''


#备忘录算法 ——采用字典（哈希表）存放，避免重复计算， 减小时间复杂度
def need_coins(k):
    if k==1 or k==3 or k==5:
        return 1
    elif k==2 or k==4:
        return 2
    else:
        return(min(map(str(k-1)),map(str(k-3)),map(str(k-5)))+1)

#建立备忘录
def map(n):
    if n in Memorandum:
        return Memorandum.get(n)
    else:
        Memorandum[n]=need_coins(int(n))
        return Memorandum.get(n)

if __name__=='__main__':
    #设定递归深度
    sys.setrecursionlimit(10000)
    Memorandum = {}
    number=input("需要的零钱：")
    n = need_coins(int(number))
    print(n)
