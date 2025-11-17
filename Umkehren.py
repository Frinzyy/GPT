a = (30 - 3) // 3

b = []
for i in range(0, 31, 3):
  b += [i]

print(b)

k = len(b)//2 
d= -1 ## Die Varieble muss draußen stehen, weil wenn es sich in der Schleife befinden würde, würde es immer auf -1 gesetzt werden ! Scope!!
for s in range (0, k):
  zwischenspeicher = b[d]
  b[d] = b[s]
  b[s] = zwischenspeicher
  d -=1 

print(b)
"""Without to create a new array, it should be alooklike this"""


