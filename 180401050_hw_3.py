import matplotlib.pyplot as plt
import sympy as sym
from sympy import Symbol
from sympy import pprint
landa=Symbol('landa')
x=Symbol('x')
e=Symbol('e')
#-sembol olan landaya değer atanmadığı icin yazı kullandım
my_f_part_1=landa**x
my_f_part_2=e**(-landa)
my_f_part_3=sym.factorial(x)
my_f=(my_f_part_1)*(my_f_part_2)/my_f_part_3
pprint(my_f)
my_f.subs({1:2}).doit().evalf()
pprint(my_f)
sym.plot(my_f.subs({landa:2,e:24}),(x,0,20),title='poisson distribution')#0-20 arası 
x_value=[]
y_value=[]
for  value in range(-5,5):
    y=my_f.subs({landa:2,e:24,x:value}).evalf()
    y_value.append(y)
    x_value.append(value)
    print(value,y)
import matplotlib.pyplot as plt
plt.plot(x_value,y_value)
    

    

