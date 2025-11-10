a = (30 - 3) // 3

b = []
c = 0
for m in range (1, a+2): # bei a addieren wir erste eins weil c mit 0 anfangt, zweite für letzte index, damit 30 auch einschließlich ist.
  c += 3
  b += [c]

print(b)

k = len(b)//2 
d= -1
for s in range (0, k):
  zwischenspeicher = b[d]
  b[d] = b[s]
  b[s] = zwischenspeicher
  d -=1 

print(b)
"""Without to create a new array, it should be alooklike this"""
