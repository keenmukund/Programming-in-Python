def insertionSort(l):
    for start in range(len(l)):
        pos=start
        while pos>0 and l[pos]<l[pos-1]:
            (l[pos],l[pos-1])=(l[pos-1],l[pos])
            pos=pos-1
        print(l)    
    print(l)
l=[5,4,3,2,1]
insertionSort(l)
