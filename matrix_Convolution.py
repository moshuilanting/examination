#该段程序实现卷积功能

#降维，高维矩阵行优先(direction=1)或列优先(direction=0)降维成一维
def m_reshape(x,direction=1):
    column=len(x[0])
    line=len(x)
    y=[]
    if direction:
        for i in range(line):
            for j in range(column):
                y.append(x[i][j])
        return y
    else:
        for j in range(column):
            for i in range(line):
                y.append(x[i][j])
        return y

#矩阵相乘，x按行降维成一排，w按列降维成一排
def multiply(x,w):
    x_reshape = m_reshape(x, 1)
    w_reshape = m_reshape(w, 0)
    y = list(map(lambda a, b: a * b, x_reshape, w_reshape))
    return sum(y)

#边缘处理，边沿镜像
def edge_processing(x,w,i,j):
    w_column=len(w[0])
    w_line=len(w)
    w_column_reshape=(w_column-1)/2
    w_line_reshape=(w_line-1)/2
    x_column=len(x[0])
    x_line=len(x)
    #返回一个a矩阵表示x[i][j]位置 的矩阵(与滤波矩阵相乘，得到滤波结果)
    a = [[0 for m in range(w_column)] for n in range(w_line)]
    for m in range(w_line):
        for n in range(w_column):
            #超出被滤波矩阵外围，镜像补足
            k1=abs(int(i+m-w_column_reshape))
            k2=abs(int(j+n-w_line_reshape))
            if k1>=x_line:
                k1=2*i-k1
            if k2>=x_column:
                k2=2*j-k2
            a[m][n]=x[k1][k2]
    return a

#卷积
def convlution(x,w):
    x_column=len(x[0])
    x_line=len(x)
    y=[[0 for i in range(x_column)]for j in range(x_line)]
    for i in range(x_line):
        for j in range(x_column):
            #得到x[i][j]位置 的矩阵a，a与w相乘的和 为(i,j)点滤波的结果
            a=edge_processing(x, w, i, j)
            #print(a)
            y[i][j]=multiply(a,w)
            #print(y)
    return y




x=[[100,100,100],[200,200,200],[0,0,0]]
w=[[0.09,0.12,0.09],[0.12,0.16,0.12],[0.09,0.12,0.09]]
y=convlution(x,w)
print(y)