# leetcode 207
#拓扑排序，检测是否有向无环图
#有环输出False，无环输出True
#根据关系e，得到入度为0的v
#用入度为0的v，去删除对应依赖v的关系
#更新v和e

#code=utf-8
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        v= [i for i in range(numCourses)]
        flag = 1
        while flag and len(v):
            flag,v,prerequisites=self.topoSort(flag,v,prerequisites)
        if flag==1:
            return True
        else :
            return False
    
    def topoSort(self,flag,v,e):
        #根据e，得到入度为0的v
        tmp = v[:] 
        for i in e:
            if i[1] in tmp:
                tmp.remove(i[1])
        print(tmp)

        if tmp == []: 
            flag=0
           
            return flag,v,e
        
        #用入度为0的v,去删除对应入度有v的关系
        for t in tmp:
            for k in range(len(e)):
                if t == e[k][0]:
                    e[k]=['remove']

        #得到新的v和e
        while ['remove'] in e:
            e.remove(['remove'])
            
        if v:
            for t in tmp:
                v.remove(t)
        
        return flag,v,e
        
            
            

if __name__=='__main__':
    a =Solution()
    answer = a.canFinish(2,[[1,0],[0,1]])
    print(answer)
