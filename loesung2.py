import hilfe
import math

def zeichne(spalten, zeilen, zeit, speicher):
  schwerpunkt_x = 19
  schwerpunkt_y = 19
  kanten_laenge = 25
  a = ((kanten_laenge/2) * ( 3 ** 0.5)) / 3 # Die Variable hilft uns beim Finden die Kordinaten von Ecken, die sich auf Koordinaten von Schwerpunkt basiert.
  x1 = schwerpunkt_x
  y1 = (19 - (2 * a))
  x2 = (19 - (25 / 2))
  y2 = (schwerpunkt_y + a)
  x3 = (19 + (25 / 2))
  y3 = y2
  x1r, y1r = rotiere_punkt(x1, y1, schwerpunkt_x, schwerpunkt_y, zeit)
  x2r, y2r = rotiere_punkt(x2, y2, schwerpunkt_x, schwerpunkt_y, zeit)
  x3r, y3r = rotiere_punkt(x3, y3, schwerpunkt_x, schwerpunkt_y, zeit)

  hilfe.dreieck(x1r, y1r, x2r, y2r, x3r, y3r, "grün", spalten, zeilen)

fps = 30
def rotiere_punkt(x, y, d1, d2, zeit):
  
  winkel = zeit / (2 * math.pi) / 30

  xn = d1 + (x - d1) * math.cos(winkel) - (y - d2) * math.sin(winkel)
  yn = d2 + (x - d1) * math.sin(winkel) + (y - d2) * math.cos(winkel)
  
  return xn, yn