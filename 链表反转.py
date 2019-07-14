# coding = utf-8
'''
from:
head 1 2 3 4 5 6 7 8 9 10
to:
head 1 2 3 6 4 5 7 8 9 10
head 1 2 3 6 5 4 7 8 9 10
head 1 2 3 6 5 4 7 8 9 10

'''
class SNode(object):
    next = None
    val = None

#创建带头结点的链表
def creatLinkList(size):
    if size<=0:
        return None
    linkList = SNode()
    pNode = linkList
    for i in range(1,size+1):
        node = SNode()
        node.val = i
        pNode.next = node
        pNode = pNode.next
    return linkList

def printLinkList(linkList):
    if linkList ==None:
        print('None')
        return
    s = 'head'
    node = linkList.next
    while node != None:
        s = s+' '+ str(node.val)
        node = node.next
    print(s)

def changelinkList(linkList,m,n):
    preMnode = linkList
    print(preMnode.val)
    for i in range(m-1):
        preMnode = preMnode.next

    for i in range(n-m):
        preNnode =linkList
        for j in range(n-1):
            preNnode = preNnode.next
        nNode = preNnode.next
        preNnode.next = preNnode.next.next
        nNode.next = preMnode.next
        preMnode.next =  nNode
        preMnode = preMnode.next
        printLinkList(linkList)


def reverselinkList(linkList):


    L,M,R = None,None,linkList

    while R.next !=None:
        L = M
        M = R
        R = R.next
        M.next=L
    R.next = M

    printLinkList(R)








if __name__ =='__main__':
    linkList =creatLinkList(10)
    printLinkList(linkList)
    reverselinkList(linkList)
    # printLinkList(linkList)
    # changelinkList(linkList,3,6)



