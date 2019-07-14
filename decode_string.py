#Given an encoded string, return it's decoded string.
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


class Solution:
    def decodeString(self, s: str) -> str:
        num=0
        stack=[]
        for i in s:
            print(stack)
            if i.isdigit():
                num=num*10+int(i)
            elif i == '[':
                stack.append(num)
                num=0
            elif i == ']':
                st = self.getnum(stack)
                stack.append(st)
            else:
                stack.append(i)
        
        return ''.join(stack)
    
    def getnum(self,stack):
        list1=[]
        for i in range(len(stack)):
            m=stack.pop()
            
            if type(m)==int:
                number=m
                break
            list1.append(m)
        list1.reverse()
        
        string = ''.join(list1)
        string = string * number
        return string
        
if __name__=='__main__':
    a=Solution()
    b=a.decodeString('3[a]2[bc]')
    print(b)
