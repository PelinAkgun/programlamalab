def power_rec(a,b):
      if b==0:
          return 1
      elif b==1:
          return a
      if b>1:
          return power_rec(a,b-1)*a
print (power_rec(3,2))   