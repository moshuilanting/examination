def quicksort(L):
    if len(L)<=1:
        return L
    return quicksort([l for l in L[1:] if l<L[0]])+L[0:1]+quicksort([r for r in L[1:] if r>=L[0]])

if __name__=='__main__':
    q=quicksort([2,4,4,4,4,1,3,4])
    print(q)                                                                        
