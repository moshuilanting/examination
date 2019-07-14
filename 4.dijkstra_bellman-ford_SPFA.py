#https://www.luogu.org/problemnew/show/P4779
#单源最短路

#leetcode 743 网络传输时间
# N个节点， 从K出发，要多久传输到整个网络。

class Solution:
    #dijkstra 308ms
    def dijkstra(self, times, N, K):
        Num=N
        
        adjacency_matrix=[[101]*N for i in range(Num)]
       
        for i in range(len(times)):
            adjacency_matrix[times[i][0]-1][times[i][1]-1]=times[i][2]
            #adjacency_matrix[times[i][1]-1][times[i][0]-1]=times[i][2]  #有向图还是无向图, 无向图翻倍
        
        for i in range(Num):
            adjacency_matrix[i][i]=0  #自己到自己时间为0
        
        Q=[]  #存放已经探索过的节点
        d=[101]* Num #存放从开始点出发的最短路，假设最远不超过101
        d[K-1]=0  #开始点
          
        while len(Q)<Num:

            #未探索过的最近节点i
            d_sort=sorted(d)
            for d_num in d_sort:
                for i in range(len(d)):
                    if d[i] == d_num:
                        if i not in Q:
                            break
                else:
                    continue
                break
            
            #维护距离，从i出发到k的距离与已知的距离做比较
            for k in range(len(d)):
                #if k not in Q: #最初的dijkstra只求不在Q中的点，如果没有这个判定也可以用于负权回路
                d[k]=min(d[k],d[i]+adjacency_matrix[i][k])
            Q.append(i)
        
        #d中存放着从K出发,到达所有点的时间，本题输出最远的值
        #if max(d)==101:
        #    return -1
        #return max(d)
        return d

    # bellman-ford 1788ms
    def bellman_ford(self, times, N, K):
        
        d=[101]*N
        d[K-1]=0
        
        for i in range(N-1):
            for j in range(len(times)):
                d[times[j][1]-1] = min(d[times[j][1]-1],d[times[j][0]-1]+times[j][2])
                #print('i:',i,'d:',d)

        for j in range(len(times)):
            if d[times[j][1]-1] > d[times[j][0]-1]+times[j][2]: #存在权为负的回路
                return -1

        return(d)

    #SPFA Shortest Path Faster Algorithm  1080ms
    def SPFA(self, times, N, K):
        d=[101]*N
        d[K-1]=0
        Q=[]
        Q.append(K-1)        
        while len(Q)>0:
            
            Q.pop(0)
            for j in range(len(times)):
                if d[times[j][1]-1]>d[times[j][0]-1]+times[j][2]:
                    d[times[j][1]-1]=d[times[j][0]-1]+times[j][2]
                    if times[j][1]-1 not in Q:
                        Q.append(times[j][1]-1)
                
                #print('i:',i,'d:',d)

        #for j in range(len(times)):
            #if d[times[j][1]-1] > d[times[j][0]-1]+times[j][2]: #存在权为负的回路
                #return -1

        return(d)
        
                
                
            
                        
                
                
    

if __name__=='__main__':
    N,S,K=map(int,input().split()) #空格分开
    L=[]
    for i in range(S):
        a,b,c=map(int,input().split())
        L.append([a,b,c])
    A=Solution()
    B=A.dijkstra(L,N,K)
    print(B)
    C=A.bellman_ford(L,N,K)
    print(C)
    D=A.SPFA(L,N,K)
    print(D)

   

        
'''
4 6 0
0 1 2
1 2 2
1 3 1
0 2 5
2 3 3
0 3 4
'''

'''
4 6 1
1 2 -1
2 3 2
2 4 1
1 3 5
3 4 3
1 4 4
'''

    
