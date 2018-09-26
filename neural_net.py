#coding=utf-8

import numpy as np

#定义非线性sigmoid函数, True为求导，False为sigmoid非线性函数
def nonlin(x,deriv=False):
    if(deriv==True):
        return(x*(1-x))
    return(1/(1+np.exp(-x)))

x = np.array([[0,0,1],
              [0,1,1],
              [1,0,1],
              [1,1,1]
              ])

y = np.array([[0],
              [1],
              [1],
              [0]])
np.random.seed(1)

#随机生成权重
w0 = 2*np.random.random((3,5))-1
w1 = 2*np.random.random((5,1))-1

for j in range(10000):
    #前向传播
    l0 = x
    l1 = nonlin(np.dot(l0,w0))
    l2 = nonlin(np.dot(l1,w1))

    #loss function
    l2_error = y -l2

    if(j%2000) == 0:
        print("error:"+ str(np.mean(np.abs(l2_error))))

    #反向传播
    l2_delta = l2_error*nonlin(l2,deriv=True)
    dw1 = np.dot(l1.T,l2_delta)
    print(dw1.shape)
    l1_error = l2_delta.dot(w1.T)
    print(l1_error.shape)
    l1_delta = l1_error*nonlin(l1,deriv=True)
    dw0 = np.dot(l0.T,l1_delta)


    w1 += l1.T.dot(l2_delta)
    w0 += l0.T.dot(l1_delta)

print(l2_delta.shape,l1.shape)
print("l2:"+str(l2))

