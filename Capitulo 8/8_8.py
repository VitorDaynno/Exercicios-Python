def mmc(a,b):
	return abs(a*b)/mdc(a,b)

def mdc(a,b):
  if a>b and b==0:
    return a
  else:
    return mdc(b,a%b)

print mmc(10,5)