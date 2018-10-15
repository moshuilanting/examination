#coding = uft-8
#给定两个字符串，求解这两个字符串的最长公共子序列（Longest Common Sequence）。比如字符串1：BDCABA；字符串2：ABCBDAB
# 则这两个字符串的最长公共子序列长度为4，最长公共子序列是：BCBA
'''
#普通递归
def LCSequence(X,Y):
    xlen = len(X)
    ylen = len(Y)
    if xlen==0 or ylen==0:
        return(0)
    elif X[xlen-1:xlen]==Y[ylen-1:ylen] and xlen>0 and ylen>0:
        return(LCSequence(X[:xlen-1],Y[:ylen-1])+1)
    elif xlen>0 and ylen>0:
        return(max(LCSequence(X[:xlen-1],Y),LCSequence(X,Y[:ylen-1])))

#动态规划备忘录算法
def mymap(x,y):
    if (x+y) in Memorandum:
        return Memorandum.get((x+y))
    else:
        Memorandum[(x+y)]=M_LCSequence(x,y)
        return Memorandum.get((x + y))

def M_LCSequence(X,Y):
    xlen = len(X)
    ylen = len(Y)
    if xlen==0 or ylen==0:
        return(0)
    elif X[xlen-1:xlen]==Y[ylen-1:ylen] and xlen>0 and ylen>0:
        return(mymap(X[:xlen-1],Y[:ylen-1])+1)
    elif xlen>0 and ylen>0:
        return(max(mymap(X[:xlen-1],Y),mymap(X,Y[:ylen-1])))

if __name__=='__main__':
    Memorandum={}
    x=input("输入第一个字符串")
    y=input("输入第二个字符串")

    n=M_LCSequence(x,y)
    print(n)

'''

#-----------------------反向思路，迭代正向求解，降低空间复杂度，输出最大公共子序列--------------
#输出所有LCS
#https://www.cnblogs.com/XueDingWen/p/EXLCS.html

def lcs(a, b):
    lena = len(a)
    lenb = len(b)
    c = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
    flag = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
    for i in range(lena):
        for j in range(lenb):
            if a[i] == b[j]:
                c[i + 1][j + 1] = c[i][j] + 1
                flag[i + 1][j + 1] = 'ok'
            elif c[i + 1][j] > c[i][j + 1]:
                c[i + 1][j + 1] = c[i + 1][j]
                flag[i + 1][j + 1] = 'left'
            elif c[i + 1][j] < c[i][j + 1]:
                c[i + 1][j + 1] = c[i][j + 1]
                flag[i + 1][j + 1] = 'up'
            #c[i + 1][j] == c[i][j + 1]时候保存向上向右两个分支
            else :
                c[i + 1][j + 1] = c[i][j + 1]
                flag[i + 1][j + 1] = 'left and up'
    return c, flag

#沿着一条路径递归，得出最长公共子序列
def printLcs(flag, a, i, j):
    if i == 0 or j == 0:
        return
    if flag[i][j] == 'ok' :
        printLcs(flag, a, i - 1, j - 1)
        st.append(a[i-1])
        print(a[i - 1], end='')
    elif flag[i][j] == 'left':
        printLcs(flag, a, i, j - 1)
    elif flag[i][j] == 'up':
        printLcs(flag, a, i-1 , j)
    else:
        print("(",end='')
        st.append("(")
        printLcs(flag, a, i, j-1)
        print("+",end='')
        st.append("+")
        printLcs(flag, a, i-1, j)
        print(")",end='')
        st.append(")")

def traceback(i,j,a,flag,st,stt):
    while(i>0 and j>0):
        if flag[i][j] == 'ok':
            st=st+a[i-1]
            i -=1
            j -=1
        else:
            if flag[i][j] == 'left':
                j -=1
            elif flag[i][j] == 'up':
                i -=1
            else:
                traceback(i-1,j,a,flag,st,stt)
                traceback(i,j-1,a,flag,st,stt)
                return
    #逆序输出
    stt.append(st[::-1])








if __name__=='__main__':
    Memorandum={}
    #a=input("输入第一个字符串")
    #b=input("输入第二个字符串")
    a = 'asdgfg'
    b = 'fgdgas'
    c, flag = lcs(a, b)
    for i in c:
        print(i)
    print('')
    for j in flag:
        print(j)
    print('')
    stt=[]
    st=''
    traceback(len(a),len(b),a,flag,st,stt)
    print(stt)
    ls=set(stt)
    [print(i) for i in ls]


