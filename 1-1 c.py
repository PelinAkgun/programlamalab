def my_f_1():
    l1=[4,-3,5,-2,-1,2,6,-2]
    maxsum=0
    for i in range(8):
        for j in range(i+1,8):
            #print(i,j)
            t=0
        for k in range(i,j):
            t=t+l1[k]
        if t>maxsum:
          maxsum=t
          i_2,j_2=i,j
    return maxsum,i_2,j_2
print(my_f_1())