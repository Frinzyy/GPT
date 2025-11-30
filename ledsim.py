import pygame as pg
import traceback

zeilen = 38
spalten = 38
fps = 30

zellenAbstand = 24
radius = 10
hintergrund = (18, 18, 18)
standardFarbe = (60, 60, 60)

randX = 40
randY = 40

farben = {
    "schwarz": (0, 0, 0),
    "weiß": (255, 255, 255), "weiss": (255, 255, 255),
    "rot": (220, 50, 47),
    "gruen": (133, 153, 0), "grün": (133, 153, 0),
    "blau": (38, 139, 210),
    "gelb": (181, 137, 0),
    "magenta": (211, 54, 130),
    "cyan": (42, 161, 152),
    "orange": (255, 128, 0),
    "lila": (108, 113, 196),
    "grau": (100, 100, 100),
    "pink": (255, 105, 180),
    "hintergrund": hintergrund,
    "standardfarbe": standardFarbe
}

breite = 2 * randX + spalten * zellenAbstand
hoehe = 2 * randY + zeilen * zellenAbstand

grid = []

def resolveFarbe(f):
    if isinstance(f, tuple) and len(f) == 3:
        r, g, b = f
        r = max(0, min(255, int(r)))
        g = max(0, min(255, int(g)))
        b = max(0, min(255, int(b)))
        return (r, g, b)
    if isinstance(f, str):
        key = f.strip().lower()
        if key in farben:
            return farben[key]
    raise ValueError(
        f"Unbekannte Farbe: {f!r}. Nutze farben {list(farben.keys())} "
        f"oder (R,G,B)."
    )

def resetGrid():
    global grid
    grid = [[standardFarbe for _ in range(spalten)] for _ in range(zeilen)]
    return grid

def setze(x, y, farbe):
    if not (0 <= x < spalten and 0 <= y < zeilen):
        raise IndexError(f"Position außerhalb des Rasters: x={x}, y={y}")
    grid[y][x] = resolveFarbe(farbe)

class Speicher:
    pass

def main():
    import loesung
    loesung.setze = setze
    loesung.farben = farben

    try:
        import hilfe
        hilfe.setze = setze
        hilfe.farben = farben
    except:
        pass

    speicher = Speicher()

    pg.init()
    screen = pg.display.set_mode((breite, hoehe))
    pg.display.set_caption("Funktionale Weihnachtsdekoration - GPT")
    clock = pg.time.Clock()

    resetGrid()
    zeit = 0
    
    if getattr(loesung, "start", None):
        loesung.start(spalten, zeilen, speicher)
    
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

        clock.tick(fps)
        resetGrid()

        if getattr(loesung, "zeichne", None):
            loesung.zeichne(spalten, zeilen, zeit, speicher)
        zeit += 1

        screen.fill(hintergrund)
        for y in range(zeilen):
            for x in range(spalten):
                cx = randX + x * zellenAbstand + zellenAbstand // 2
                cy = randY + y * zellenAbstand + zellenAbstand // 2
                pg.draw.circle(screen, grid[y][x], (cx, cy), radius)

        pg.display.flip()

    pg.quit()

if __name__ == "__main__":
    main()
    
