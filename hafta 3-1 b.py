def lookup(d,V):
    for k in d:
      if d[k]==V:
          return k
    return -1
print(lookup([2,5],3))