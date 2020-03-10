from sympy import FiniteSet
s=FiniteSet(1,1.5,Fraction(1,5),1,1.5)
t=FiniteSet(Fraction(1,5),1.5,1,1)
for member in s:
    print(member)
if s==t:
    print("true")
else:
    print("false")