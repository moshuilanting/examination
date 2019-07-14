#You are given coins of different denominations and a total amount of money amount.
#Write a function to compute the fewest number of coins that you need to make up that amount.
#If that amount of money cannot be made up by any combination of the coins, return -1.

'''
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1
'''

'''
#递归常用思路
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount <1: 
            return 0
        
        m=[0] * amount
        return self.count(coins,amount, m)
        
    #建立一个列表c，长度为要计算的amount，备忘录，用于存储对应值的最少币数。
    def count(self, coins, rem, c):
        if rem<0: return -1
        if rem==0: return 0
        if c[rem-1]!=0: return c[rem-1]
        h=21472147
        for coin in coins:
            res = self.count(coins,rem-coin,c)
            if res>=0 and res <h:
                h=1+res
        
        if h==21472147:
            c[rem-1]=-1
        else:
            c[rem-1] =h
        return c[rem-1]
        
'''

'''
#针对这个找零问题的快速算法
class Solution:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        self.number=21472147
        coins=sorted(coins,reverse=True)
        self.count(coins,amount,0)
        if self.number==21472147:
            self.number =-1
        return self.number 
        
    
    def count(self, coins, amount,n):
        print(coins[0])
        print("------coins: ", coins," self.number: ",self.number, "amount//coins[0]:",amount//coins[0],"n:",n, "len(coins):",len(coins))
        input()
        if len(coins)==1:
            if amount%coins[0]==0:
                self.number=min(self.number,amount/coins[0]+n)
            return
            
        for i in range(amount//coins[0],-1,-1):
            print("i：",i,"n+i: ", n+i,"coins[0]",coins[0])
            if n+i>=self.number:
                return
            self.count(coins[1:],amount-i*coins[0],n+i)
'''
'''
class Solution:
    def __init__(self):
        self.Memorandum={}
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        answer=self.count(coins,amount)
        if answer>=21472147:
            return -1
        else:
            return answer
        
    
    def count(self,coins,amount):
        a=[]
        for i in range(len(coins)):
            if amount==coins[i]:
                return 1
            elif amount>coins[i]:
                a.append(self.map(coins,str(amount-coins[i])))
            else:
                a.append(21472147)
        
        q=min(a)
        return q+1
            
    def map(self,coins,n):
        if n in self.Memorandum:
            return self.Memorandum.get(n)
        else:
            self.Memorandum[n]=self.count(coins,int(n))
            return self.Memorandum.get(n)
'''


if __name__=='__main__':
    A= Solution()
    B=A.coinChange([1,2,5],11)
    print(B)  
