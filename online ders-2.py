
from sympy import Symbol

x=Symbol('x')
y=Symbol('y')
p=x*(x+x)
#print(p)
p=(x+2)*(x+3)
#print(p)

x=Symbol('x')
Series=x
n=5
for i in range(2,n+1):
    Series=Series+(x**i)/i 
    #print(Series)
from sympy import pprint
#pprint(Series)

x=Symbol('x')
y=Symbol('y')
expr=x*x+x*y+x*y+y*y
res=expr.subs({x:1,y:2})
r=expr.subs({x:1-y})
#print(r)

import sympy as sym
from sympy import Symbol
from sympy import pprint
import sympy.plotting as syp
sigma=Symbol('sigma')
mu=Symbol('mu')
#pprint(2*sym.pi*sigma)
gauss_function=1/sym.sqrt(2*sym.pi*sigma)
gauss_function.subs({mu:0,sigma:1})
#print(gauss_function)
part_1=1/(sym.sqrt(2*sym.pi*sigma**2))
part_2=sym.exp(-1*((x-mu)**2)/(2*sigma**2))
#pprint(1/(sym.sqrt(2*sym.pi*sigma**2)))
my_gauss_f=part_1*part_2
syp.plot(my_gauss_f.subs({mu:1,sigma:3}),(x,-10,10),title='gauss')

x_values=[]
y_values=[]
for value in range (-5,5):
    y=my_gauss_f.subs({mu:10,sigma:30,x:value})
    y_values.append(y)
    x_values.append(value)
    print(x,y)
import matplotlib.pyplot as plt
plt.plt(x_values,y_values)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    