import sys

a = int(sys.argv[1])
b = int(sys.argv[2])


print(" ",end="\t")
for i in range(a, b+1):
  print(i ,end="\t")
print("")
""" Das Kopf der Tabelle wurde mit den Zeilen erstellt, die da oben stehen. Wir müssen die oben stehende Zeile eine Leerzeile ausgeben lassen, damit die letztes Element, das vom Range Funktion kommt, nicht mehr im Effekt von "end="\t"" steht,(sonst zweite Zeile von der Multiplikationstabelle schreibt man neben der ersten Zeile). """

for m in range(a, b+1):
  print(m, end="\t")
  for n in range(a, b+1):
    print(m*n, end="\t")
  print("")


""" Ich habe mal nachgeschaut, wo mein Code eine Störung anzeigt, wie bei dem Code für die erste Zeile der Multiplikationstabelle muss ich am jeden Anfang der Zeile drauf achten, dass nach dem letzten Element der Zeile ich ein leeres String ausbasteln lassen muss, sonst die Tabelle sieht nicht richtig aus. """


"""
Today's Learning:

- effektive Lösung finden
- die effektive Nutzung von end="\t"
- for Schleifen:
- Kommandozeilenparameter nutzen

"""