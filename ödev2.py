import operator
dosya=open("D://input_hw_2.csv","r")
icerik=dosya.read()
kelimelistesi=icerik.split("\n")
print(kelimelistesi[1])
frekans=dict()
n=len(kelimelistesi)-1
for i in range(0,n):
    wl2=kelimelistesi[i].split(";")
    #print(wl2[3])
    wl3=wl2[3].split("-")   
    #print(wl3[1])
    ay=int(wl3[1])
    #print(ay)
    if(ay in frekans):
        frekans[ay]=frekans[ay]+1
    else:
        frekans[ay]=1
    #print(frekans)
sorted_frekans=sorted(frekans.items(),key=operator.itemgetter(1))
#print("sirali hali")
#print(sorted_frekans)
n2=len(sorted_frekans)
if(n2%2!=0):
    medyan=sorted_frekans[int(n2/2)][1]
    print("medyan:" + str(medyan))
else:
    medyan=sorted_frekans[n2/2-1][1]
   # print(medyan)
kisi=n2
top=0
for i in sorted_frekans:
    top+=i[1]
ort=top/kisi
print("ortalama" + str(ort))
f=open("180401050_hw_2_output.txt","w") 
f.write("medyan:" + str(medyan)+"\n")
f.write("ortalama:"+str(ort))
f.close()