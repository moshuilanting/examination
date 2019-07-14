class Solution:
    def mergeKLists(self, lists):
        k= len(lists)
        heap= [0]*k
        L = 0
        for l in lists:
            L +=len(l)
        head=[]
        for j in range(L): 
            merge_list=[]
            for i in range(k):
                #print(j,i,heap[i])
                if heap[i] >= len(lists[i]):
                    merge_list.append(123123123123)
                else:
                    merge_list.append(lists[i][heap[i]])
            i=merge_list.index(min(merge_list))
            heap[i]+=1
            head.append(merge_list[i])
            print(merge_list,head)
        
        return head

if __name__=='__main__':
    a=Solution()
    b=a.mergeKLists([[1,4,5],[1,3,4],[2,6]])
    print(b)
