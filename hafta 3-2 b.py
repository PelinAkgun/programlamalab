def probabilty(space,event):
    return len(event)/len(event)
#asal olup olmadığını kontrol eder
def checkprime(number):
    if number!=1:
        for factor in range(2,number):
            if number%factor==0:
                return False
            else:
                return True
        return True
#print(checkprime(1))
        
    
space=FiniteSet(*range(1,21))
    #liste olarak almasın,virgülle ayrılmış elemana dönüştürsün diye * koyduk
primes=[]
    #append i kullanmak için gerekli
for num in space:
     if checkprime(num):
        primes.append(num)
event=FiniteSet(*primes)
p=probabilty(space,event)
print(p)
    