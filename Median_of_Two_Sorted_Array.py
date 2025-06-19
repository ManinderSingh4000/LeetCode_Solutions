
def median_of_arrays(a , b):

    c = a+ b
    c = sorted(c)
    
    mid = len(c)//2
    
    if len(c)%2 ==1:
        print(c[mid])
    else:
        print((c[mid-1]+c[mid])/2)
    
    print(c)
    
# median_of_arrays([1,5,2,3] , [2,4,3,6])
# median_of_arrays([1,3] , [2])
median_of_arrays([1,2] , [4,3])
