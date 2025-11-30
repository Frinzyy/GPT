import math

def kreis(mittelX, mittelY, radius, farbe, spalten, zeilen):
    bboxMinX = int(mittelX - radius)
    bboxMaxX = int(mittelX + radius)
    bboxMinY = int(mittelY - radius)
    bboxMaxY = int(mittelY + radius)

    r2 = radius * radius
    for y in range(bboxMinY, bboxMaxY + 1):
        for x in range(bboxMinX, bboxMaxX + 1):
            dx = x - mittelX
            dy = y - mittelY
            if dx*dx + dy*dy <= r2:
                if 0 <= x < spalten and 0 <= y < zeilen:
                    setze(x, y, farbe)
                    
def rechteck(x0, y0, x1, y1, farbe, spalten, zeilen):
    linie(x0, y0, x0, y1, farbe, spalten, zeilen)
    linie(x0, y1, x1, y1, farbe, spalten, zeilen)
    linie(x1, y1, x1, y0, farbe, spalten, zeilen)
    linie(x1, y0, x0, y0, farbe, spalten, zeilen)
    
def linie(x0, y0, x1, y1, farbe, spalten, zeilen):
    x0 = int(round(x0))
    y0 = int(round(y0))
    x1 = int(round(x1))
    y1 = int(round(y1))
    
    dx = abs(x1 - x0)
    dy = -abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx + dy
    
    x, y = x0, y0
    while True:
        if 0 <= x < spalten and 0 <= y < zeilen:
            setze(x, y, farbe)
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x += sx
        if e2 <= dx:
            err += dx
            y += sy

def flaeche_dreieck(x1, y1, x2, y2, x3, y3):
  flaeche = (1/2) * ((x1*(y2-y3)) + (x2 * (y3-y1)) + (x3 * (y1-y2)))  
  if flaeche < 0:
    flaeche = -flaeche
  return flaeche
#Falls die Flaeche negativ rauskommt, intervieren wir den Wert

def baryzentrische_Kordinaten(x1, y1, x2, y2, x3, y3, p1, p2):
  FA = flaeche_dreieck(x1, y1, x2, y2, x3, y3)
  FA1 = flaeche_dreieck(x1, y1, x2, y2, p1, p2)
  FA2 = flaeche_dreieck(x2, y2, x3, y3, p1, p2)
  FA3 = flaeche_dreieck(x1, y1, x3, y3, p1, p2)
  return (FA1 / FA <= 1 and FA2 / FA <= 1 and FA3 / FA <= 1) and (((FA1 / FA) + (FA2 / FA) + (FA3 / FA))) - 1 < 0.0001

def dreieck(x1, y1, x2, y2, x3, y3, farbe, spalten, zeilen):
  for x in range(spalten):
    for y in range(zeilen):
      if baryzentrische_Kordinaten(x1, y1, x2, y2, x3, y3, x, y):
        setze(x, y, farbe)
  