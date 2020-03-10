def my_f_2(list_1=[4,-3,5,-2,-1,2,6,-2]):
    n=len(list_1)
    maxsum=0
    for i in range(n):
        t=0
        for j in range(i,n):
            t=t+list_1[j]
            if (t>maxsum):
                maxsum=t
    return maxsum
print(my_f_2())
    
            