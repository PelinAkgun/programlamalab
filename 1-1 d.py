def my_f_2():
    l1=[4,-3,5,-2,-1,2,6,-2]
    maxsum=0
    t=0
    for i in range(8):
        for j in range(i,8):
            t=t+l1[j]
            if t>maxsum:
                maxsum=t
                i_2,j_2=i,j
    return maxsum,i_2,j_2
print(my_f_2())