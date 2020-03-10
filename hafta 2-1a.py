def my_f_1(list_1=[4,-3,5,-1,-2,2,6,-2]):
    n=len(list_1)
    maxsum=0
    for i in range(n):
        for j in range(i,n):
            #print(i,j)
            t=0
            for k in range(i,j):
                t=t+list_1[k]
                if(t>maxsum):
                    maxsum=t
    return maxsum
print(my_f_1())