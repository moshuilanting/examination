#3*3的方格内有编号1-8的方块，求最少的步数，恢复这些方块的顺序，广度优先
import time

class solution:
    def __init__(self):
        self.hashmap1=[0]*99381
        self.hashmap2=[0]*99382
        self.f=0

        
    #广度优先计算最少步
    def search_steps(self,start,end):
        Q=[]
        Q.append(start)
        ans =0
        if start==end:
            return ans
        while len(Q)>0:
            P=Q[:]
            #print('Q:',Q)
            Q=[]
            #print(ans)
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
            ans +=1 #搜索步骤 +1
                        
    #检测是否是重复状态，这样还是会有一定的容错率
    def repetition(self,S):
        int_S=int(S)
        if self.hashmap1[int_S%99381]==1 and self.hashmap2[int_S%99382]==1:
            return 1 #状态重复
        else:
            self.hashmap1[int_S%99381]=1
            self.hashmap2[int_S%99382]=1
            return 0


    def two_way_repetition(self,S,F):
        int_S=int(S)
        #正向
        if F==0:
            if self.hashmap1[int_S%99381]==1 and self.hashmap2[int_S%99382]==1:
                return 1
            elif self.hashmap1[int_S%99381]==2 and self.hashmap2[int_S%99382]==2:
                self.f=1
                return 1
            else:
                self.hashmap1[int_S%99381]=1
                self.hashmap2[int_S%99382]=1
                return 0

        #反向1
        if F==1:
            if self.hashmap1[int_S%99381]==2 and self.hashmap2[int_S%99382]==2:
                return 1
            elif self.hashmap1[int_S%99381]==1 and self.hashmap2[int_S%99382]==1:
                self.f=1
                return 1
            else:
                self.hashmap1[int_S%99381]=2
                self.hashmap2[int_S%99382]=2
                return 0

    def two_way_search(self,start,end):

        ans =0
        if start==end:
            return ans
        
        #正向
        Q=[]
        Q.append(start)
        #逆向
        W=[]
        W.append(end)


        while len(Q)>0 and len(W)>0:
            
            #正向
            P=Q[:]
            Q=[]
            for k in range(len(P)):
                ST=P.pop(0)
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
                    flag=self.two_way_repetition(S,0)
                    if flag==0:
                        Q.append(S)
                    #print('up:','ST',ST,'S',S,'flag',flag)
                if down>=0 and down <9:
                    tmp_1=ST[i]
                    tmp_2=ST[down]
                    S=ST.replace(ST[i],'9')
                    S=S.replace(ST[down],tmp_1)
                    S=S.replace('9',tmp_2)
                    flag=self.two_way_repetition(S,0)
                    if flag==0:
                        Q.append(S)
                    #print('down:','ST',ST,'S',S,'flag',flag)     
                if left>=0 and left <9 and i%3!=0:
                    tmp_1=ST[i]
                    tmp_2=ST[left]
                    S=ST.replace(ST[i],'9')
                    S=S.replace(ST[left],tmp_1)
                    S=S.replace('9',tmp_2)
                    flag=self.two_way_repetition(S,0)
                    if flag==0:
                        Q.append(S)
                    #print('left:','ST',ST,'S',S,'flag',flag)
                if right>=0 and right <9 and i%3!=2:
                    tmp_1=ST[i]
                    tmp_2=ST[right]
                    S=ST.replace(ST[i],'9')
                    S=S.replace(ST[right],tmp_1)
                    S=S.replace('9',tmp_2)
                    flag=self.two_way_repetition(S,0)
                    if flag==0:
                        Q.append(S)
                    #print('right:','ST',ST,'S',S,'flag',flag) 
            ans +=1 #搜索步骤 +1
            if self.f==1:
                return ans

            #逆向
            P=W[:]
            W=[]
            for k in range(len(P)):
                ST=P.pop(0)
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
                    flag=self.two_way_repetition(S,1)
                    if flag==0:
                        W.append(S)
                    #print('up:','ST',ST,'S',S,'flag',flag)
                if down>=0 and down <9:
                    tmp_1=ST[i]
                    tmp_2=ST[down]
                    S=ST.replace(ST[i],'9')
                    S=S.replace(ST[down],tmp_1)
                    S=S.replace('9',tmp_2)
                    flag=self.two_way_repetition(S,1)
                    if flag==0:
                        W.append(S)
                    #print('down:','ST',ST,'S',S,'flag',flag)     
                if left>=0 and left <9 and i%3!=0:
                    tmp_1=ST[i]
                    tmp_2=ST[left]
                    S=ST.replace(ST[i],'9')
                    S=S.replace(ST[left],tmp_1)
                    S=S.replace('9',tmp_2)
                    flag=self.two_way_repetition(S,1)
                    if flag==0:
                        W.append(S)
                    #print('left:','ST',ST,'S',S,'flag',flag)
                if right>=0 and right <9 and i%3!=2:
                    tmp_1=ST[i]
                    tmp_2=ST[right]
                    S=ST.replace(ST[i],'9')
                    S=S.replace(ST[right],tmp_1)
                    S=S.replace('9',tmp_2)
                    flag=self.two_way_repetition(S,1)
                    if flag==0:
                        W.append(S)
                    #print('right:','ST',ST,'S',S,'flag',flag)

            ans +=1 #搜索步骤 +1
            if self.f==1:
                return ans
            #print('Q:',Q,'W:',W,'ans:',ans)
        
        

    
    #深度优先，得出是哪几步,n从1开始增加，也可以算出最少的步数
    def find_steps(self,n,Q,start,end):
        if start==end:
            print('finish:',Q)
        Q.append(start)

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
            self.find_steps(n-1,Q,S,end)
            Q.pop(-1)
        





if __name__=='__main__':
    start = '082175634'
    end = '123456780'
    time_start = time.clock()

    calc=solution()
    ans=calc.search_steps(start,end)
    print('ans:',ans)

    #a=calc.two_way_search(start,end)
    #print('ans:',a)
    #calc.find_steps(ans,[],start,end)
    
    time_end = time.clock()
    print(time_end-time_start)
    
    
