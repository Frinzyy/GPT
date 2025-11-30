import hilfe

def zeichne(spalten, zeilen, zeit, speicher):
    hilfe.dreieck(spalten//2,0, 0, zeilen-1, 
                  spalten-1,zeilen-1, "grün", 
                  spalten, zeilen)