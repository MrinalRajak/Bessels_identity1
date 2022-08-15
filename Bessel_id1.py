
#BESSEL'S IDENTUTY1

#(1)jn(-n,x) = (-1)^n*jn(n,x)

import numpy as np
from scipy.special import jn
from scipy.integrate import quad
from scipy.misc import derivative

n=int(input("Enter the n: "))
x=float(input("Enter the x: "))
LHS=jn(-n,x)
RHS=(-1)**n*jn(n,x)
print("LHS: ",LHS)
print("RHS: ",RHS)
