#https://ac.nowcoder.com/acm/contest/76/B?&headNav=www&headNav=acm
#来源：牛客网

#测试输入包含多条测试数据
#每个测试数据的第1行分别给出可用的经费c(<1000000)，道路数目n(n<10000)，
#以及城市数目m(<100)。
#接下来的n行给出建立公路的成本信息，每行给出三个整数，
#分别是相连的两个城市v1、v2(0<v1,v2<=m)以及建设公路所需的成本h(h<100)。

#最小生成树

if __name__ == '__main__':
    c,n,m = map(int,input().split())
    the_matrix=[[21472147]*m for i in range(m)]

    for i in range(n):
        x,y,z=map(int,input().split())
        if the_matrix[x-1][y-1]>z:
            the_matrix[x-1][y-1]=z
        #the_matrix[y-1][x-1]=z

    for i in range(m):
        the_matrix[i][i]=0
        
    #print(the_matrix)

    D=0 #存放计算最小经费（权重），每次循环更新
    Q=set()
    P=set(range(m))
    Q.update([0])
    
    while len(Q)<len(P):
        d=[0,0,21472147]
        for i in Q:
            for j in P-Q:
                if d[2] > the_matrix[i][j]:
                    d=[i,j,the_matrix[i][j]]
        D+=d[2]
        Q.update([j])
    if D<=c:
        print('Yes')
    else:
        print('No')
                    
            
                
              
            
      
'''
20 10 5
1 2 6
1 3 3
1 4 4
1 5 5
2 3 7
2 4 7
2 5 8
3 4 6
3 5 9
4 5 2
yes
'''
