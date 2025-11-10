import sys
import math

a = int(sys.argv[1])
prim = True

for i in range(2, int(math.sqrt(a))+1):
  if a % i == 0: 
    prim = False
    break
print(prim)