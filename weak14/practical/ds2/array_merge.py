#there are two sorted array we need to merge these array to sorted list
a=[10,20,30,40,50]
b=[2,3,4,5,35]
def merge_sort(a,b):
    l1,l2= len(a),len(b)
    i,j,k = 0,0,0
    merged=[0]*(l1+l2)
    while i < l1 and j < l2 :
        if a[i] < b[j]:
            merged[k] = a[i]
            i+=1
        else :
            merged[k] = b[j]
            j+=1
        k+=1
    while i < l1 :
        merged[k] = a[i]
        i+=1
        k+=1
    while j <l2 :
        merged[k] = a[j]
        j+=1
        k+=1
    print(merged)
    
merge_sort(a,b)
    