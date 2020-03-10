
def my_buble(list_1):
    list_1=[4,-3,5,-2,-1,2,6,-2]
    for  i in range(len(list_1),0,-1):
        for j in range(i):
            if list_1[j]>list_1[j+1]:
                t=list_1[j+1]
                list_1[j+1]=list_1[j]
                list_1[j]=t
    return list_1
print(my_buble([4,-3,5,-2,-1,2,6,-2]))