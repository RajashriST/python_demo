#factorial

fact=1
def factorial(x):
  if x>1:
  	return x*factorial(x-1)
  elif x==1:
    return 1
fact=factorial(6)
print(fact)


#import math
#print(math.factorial(5))

