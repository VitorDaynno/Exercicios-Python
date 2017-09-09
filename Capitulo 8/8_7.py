def mdc(a,b):
  if a>b and b==0:
    return a
  else:
    return mdc(b,a%b)

print(mdc(100,60))

