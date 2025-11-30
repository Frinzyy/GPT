import hilfe
import math
from loesung2 import rotiere_punkt


def punkt_auf_kreis(radius, cx, cy, winkel):
  x = cx + radius * math.cos(winkel)
  y = cy + radius * math.sin(winkel)
  return x, y

def zeichne(spalten, zeilen, zeit, speicher):
  radius = 30
  cx, cy = 19, 19
  farben = ["schwarz", "weiß", "rot", "blau", "pink", "orange", "lila"]

  for i in range(7):
    winkel1 = zeit / 30 + i * ((2 * math.pi) / 7)
    winkel2 = zeit / 30 + (i +1) * ((2 * math.pi) / 7)
 
    x1, y1 = punkt_auf_kreis(radius, cx, cy, winkel1)
    x2, y2 = punkt_auf_kreis(radius, cx, cy, winkel2)
  
    hilfe.dreieck(x1, y1, x2, y2, cx, cy, farben[i], spalten, zeilen)