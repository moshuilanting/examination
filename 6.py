#3*3的方格内有编号1-8的方块，求最少的步数，恢复这些方块的顺序，广度优先
import time

class solution:
    def __init__(self):
        self.hashmap1=[0]*603  #用于广度优先搜索
        self.hashmap2=[0]*604  #用于广度优先搜索

        self.hashmap3=[0]*603  #用于深度优先搜索
        self.hashmap4=[0]*604  #用于深度优先搜索

        
    #广度优先计算最少步
    def search_steps(self,start,end):
        Q=[]
        Q.append(start)
        ans =0
        if start==end:
            return ans
        
        while len(Q)>0:
            P=Q[:]
            Q=[]
            
            for k in range(len(P)):
                ST=P.pop(0)
                if ST==end:
                    return ans
                
                i=ST.find('0')
                up=i-3
                down=i+3
                left=i-1
                right=i+1

                if up>=0 and up <9:
                    tmp_1=ST[i]
                    tmp_2=ST[up]
                    S=ST.replace(ST[i],'9')
                    S=S.replace(ST[up],tmp_1)
                    S=S.replace('9',tmp_2)
                    flag=self.repetition(S)
                    if flag==0:
                        Q.append(S)
                    #print('up:','ST',ST,'S',S,'flag',flag)
                if down>=0 and down <9:
                    tmp_1=ST[i]
                    tmp_2=ST[down]
                    S=ST.replace(ST[i],'9')
                    S=S.replace(ST[down],tmp_1)
                    S=S.replace('9',tmp_2)
                    flag=self.repetition(S)
                    if flag==0:
                        Q.append(S)
                    #print('down:','ST',ST,'S',S,'flag',flag)     
                if left>=0 and left <9 and i%3!=0:
                    tmp_1=ST[i]
                    tmp_2=ST[left]
                    S=ST.replace(ST[i],'9')
                    S=S.replace(ST[left],tmp_1)
                    S=S.replace('9',tmp_2)
                    flag=self.repetition(S)
                    if flag==0:
                        Q.append(S)
                    #print('left:','ST',ST,'S',S,'flag',flag)
                if right>=0 and right <9 and i%3!=2:
                    tmp_1=ST[i]
                    tmp_2=ST[right]
                    S=ST.replace(ST[i],'9')
                    S=S.replace(ST[right],tmp_1)
                    S=S.replace('9',tmp_2)
                    flag=self.repetition(S)
                    if flag==0:
                        Q.append(S)
                    #print('right:','ST',ST,'S',S,'flag',flag)
            print(ans,Q)
            ans += 1 #搜索步骤 +1
            if ans%1000==0:
                print(ans)
                        
    #检测是否是重复状态
    def repetition(self,S):
        int_S=int(S)
        if self.hashmap1[int_S%603]==1 and self.hashmap2[int_S%604]==1:
            return 1 #状态重复
        else:
            self.hashmap1[int_S%603]=1
            self.hashmap2[int_S%604]=1
            return 0


    def two_way_search(self,start,end):
        pass


    #深度优先，得出是哪几步
    def find_steps(self,n,Q,start,end):

        if start==end:
            print('finish:',Q,n)
            
        Q.append(start)
        print(Q)

        if n==0:
            return
        
        
        ST=Q[-1]
        i=ST.find('0')
        up=i-3
        down=i+3
        left=i-1
        right=i+1
        
        if up>=0 and up <9:
            tmp_1=ST[i]
            tmp_2=ST[up]
            S=ST.replace(ST[i],'9')
            S=S.replace(ST[up],tmp_1)
            S=S.replace('9',tmp_2)
            flag=self.repetition(S)
            #print('up:','ST',ST,'S',S,'flag',flag)
            if flag==0:
                #print('up:','ST',ST,'S',S,'flag',flag)
                self.find_steps(n-1,Q,S,end)
                Q.pop(-1)
            
        if down>=0 and down <9:
            tmp_1=ST[i]
            tmp_2=ST[down]
            S=ST.replace(ST[i],'9')
            S=S.replace(ST[down],tmp_1)
            S=S.replace('9',tmp_2)
            flag=self.repetition(S)
            #print('down:','ST',ST,'S',S,'flag',flag)
            if flag==0:
                #print('down:','ST',ST,'S',S,'flag',flag)
                self.find_steps(n-1,Q,S,end)
                Q.pop(-1)
            
        if left>=0 and left <9 and i%3!=0:
            tmp_1=ST[i]
            tmp_2=ST[left]
            S=ST.replace(ST[i],'9')
            S=S.replace(ST[left],tmp_1)
            S=S.replace('9',tmp_2)
            flag=self.repetition(S)
            #print('left:','ST',ST,'S',S,'flag',flag)
            if flag==0:
                #print('left:','ST',ST,'S',S,'flag',flag)
                self.find_steps(n-1,Q,S,end)
                Q.pop(-1)
            
        if right>=0 and right <9 and i%3!=2:
            tmp_1=ST[i]
            tmp_2=ST[right]
            S=ST.replace(ST[i],'9')
            S=S.replace(ST[right],tmp_1)
            S=S.replace('9',tmp_2)
            flag=self.repetition(S)
            #print('right:','ST',ST,'S',S,'flag',flag)
            if flag==0:
                #print('right:','ST',ST,'S',S,'flag',flag)
                self.find_steps(n-1,Q,S,end)
                Q.pop(-1)
            
        
        
        
        





if __name__=='__main__':
    start = '123475086'
    end = '123456780'
    time_start = time.clock()

    calc=solution()
    ans=calc.search_steps(start,end)
    print('ans:',ans)

    #calc.find_steps(10,[],start,end)
    
    
    time_end = time.clock()
    print(time_end-time_start)
    
    
    
