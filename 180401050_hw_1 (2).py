import operator
dosya=open("D://input.txt","r")
tumkelimeler=dosya.read()
sayac=dict()
kelimelistesi=tumkelimeler.lower().split()
#print(kelimelistesi[2])

c=dict()
for  i in kelimelistesi:
    if i in sayac:
        sayac[i]+=1
    else:
        sayac[i]=1
#for j in sayac:
  # print(j,sayac[j])
girilen=input("input gir")
list_1=girilen.split()
'''
for a in kelimelistesi:
    if(a==girilen):
        c[a+1]+=1
        c.key=c[a+1]

'''
for i in kelimelistesi:
    temp=(len(list_1))
   # print(temp)
    if temp>4:
     #  print("overload")
       break
       
    if(list_1[temp-1]==i):
        word=kelimelistesi[kelimelistesi.index(i)+1]
       # print("kelime:",word)
        kelimelistesi.remove(i)
        if word in sayac:
            sayac[word]+=1
        else:
             sayac[word]=1            
        
if (len(sayac)==0):
   result=("öneri yok")
else:
   result=(max(sayac.items(),key=operator.itemgetter(1))[0])
       
dosya_2=open("output.txt","w")
dosya_2.write(result)
dosya_2.close 
        #print(kelimelistesi[kelimelistesi.index(i)+1])
