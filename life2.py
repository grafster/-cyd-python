"""
Conway's Game of Life — Cheap Yellow Display (CYD)
480 x 320 pixels, 10 x 10 pixel cells → 48 x 32 grid
MicroPython
"""

import random
import time
import st7789_base, st7789_ext as st7789
from machine import freq, Pin, SPI

class TestTFT:
    def rect(self,x,y,w,h,color,fill=False):
        print (f'rect {x},{y},{w},{h},{color}')
    def circle(self, x, y, radius, color, fill=False):
        print('circle')
    def line(self, x0, y0, x1, y1, color):
        print(f'line {x0} {y0} {x1} {y1}')
    def triangle(self, x0, y0, x1, y1, x2, y2, color, fill=False):
        print('triangle')
    def color(self, x,y,z):
        print(f'color {x} {y} {z}')
        return 42
    def pixel(self,x,y,color):
        print(f'pixek {x} {y} {color}')
    
    
# ── Display dimensions & cell size ───────────────────────────────────────────
W = 480
H   = 320
CELL   = 20
COLS   = W // CELL   # 48
ROWS   = H // CELL   # 32

# ── Colours — initialised in run() once tft is available ─────────────────────
BLACK = None
ALIVE = None
DEAD  = None
GRID  = None

def init_colours(tft):
    global BLACK, ALIVE, DEAD, GRID
    BLACK = tft.color(  0,   0,   0)
    ALIVE = tft.color( 80, 220, 120)   # bright green cells
    DEAD  = tft.color( 10,  20,  10)   # very dark green background
    GRID  = tft.color( 25,  40,  25)   # subtle grid lines

def debugOut(tft, text):
    tft.text(10,295,text, tft.color(255,255,255), tft.color(0,0,0))
    tft.text(10,305,text, tft.color(0,0,0), tft.color(255,255,255))

# ── Grid helpers ──────────────────────────────────────────────────────────────
def make_grid():
    return [0] * (COLS * ROWS)

def idx(col, row):
    return row * COLS + col

def randomise(grid, density=0.35):
    for i in range(len(grid)):
        grid[i] = 1 if random.random() < density else 0

def count_neighbours(grid, col, row):
    total = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            r = (row + dr) % ROWS
            c = (col + dc) % COLS
            total += grid[idx(c, r)]
    return total

def step(grid, next_grid):
    for row in range(ROWS):
        for col in range(COLS):
            n = count_neighbours(grid, col, row)
            alive = grid[idx(col, row)]
            if alive:
                next_grid[idx(col, row)] = 1 if n in (2, 3) else 0
            else:
                next_grid[idx(col, row)] = 1 if n == 3 else 0

# ── Drawing ───────────────────────────────────────────────────────────────────
def draw_cell(tft, col, row, alive):
    """Draw a single cell with a 1-pixel grid border."""
    x = col * CELL
    y = row * CELL
    
    tft.rect(x+2, y+2, CELL-4, CELL-4, tft.color(0,0,128) if alive else tft.color(0,128,0), True)
#    tft.rect(x, y, CELL - 1, CELL - 1, ALIVE if alive else DEAD, True)
#    tft.rect(x + CELL - 1, y, 1, CELL, GRID, True)
#    tft.rect(x, y + CELL - 1, CELL, 1, GRID, True)

def draw_full(tft, grid):
    tft.rect(0, 0, W, H, GRID, True)   # grid colour fills the gaps
    for row in range(ROWS):
        for col in range(COLS):
            draw_cell(tft, col, row, grid[idx(col, row)])

def draw_diff(tft, old_grid, new_grid):
    for row in range(ROWS):
        for col in range(COLS):
            i = idx(col, row)
            if old_grid[i] != new_grid[i]:
                draw_cell(tft, col, row, new_grid[i])

# ── Main loop ─────────────────────────────────────────────────────────────────
def run(tft, stagnation_limit=10, pause_ms=60):
    init_colours(tft)
    grid      = make_grid()
    next_grid = make_grid()
    prev_grid = make_grid()  # snapshot from the generation before

    run_number = 1

    while True:
        #print("Run {}: randomising grid...".format(run_number))
        randomise(grid)
        draw_full(tft, grid)
        generation = 0
        stagnant   = 0

        while True:
            # Save current grid BEFORE stepping so we can compare
            for i in range(len(grid)):
                prev_grid[i] = grid[i]

            step(grid, next_grid)
            generation += 1

            draw_diff(tft, grid, next_grid)

            # Swap next_grid into grid
            for i in range(len(grid)):
                grid[i] = next_grid[i]

            alive = sum(grid)
            print("Gen {:4d}  alive: {:4d}".format(generation, alive))

            if alive == 0:
                print("Extinct - restarting.")
                break

            # Compare new grid against the one from the previous generation
            changed = any(grid[i] != prev_grid[i] for i in range(len(grid)))
            if not changed:
                stagnant += 1
                if stagnant >= stagnation_limit:
                    print("Stagnant - restarting.")
                    break
            else:
                stagnant = 0

            time.sleep_ms(pause_ms)

        run_number += 1



display = st7789.ST7789(
    SPI(1, baudrate=40000000, phase=0, polarity=0),
    480, 320,
    reset=Pin(1, Pin.OUT),
    dc=Pin(2, Pin.OUT),
    cs=Pin(15, Pin.OUT),
)

display.init(landscape=True,mirror_y=False,inversion=False)
backlight = Pin(27,Pin.OUT)
backlight.on()
display.fill(display.color(255,0,0))
display.rect(20,20, 20, 20, display.color(0,0,0), True)
debugOut(display, 'potto')
draw_cell(display, 1, 1, True)
draw_cell(display, 1, 2, False)
run(display)
#run(creteDisply())

# ── Entry point ───────────────────────────────────────────────────────────────
# from machine import Pin, SPI
# import ili9341
# spi = SPI(1, baudrate=40_000_000, sck=Pin(14), mosi=Pin(13))
# tft = ili9341.ILI9341(spi, cs=Pin(15), dc=Pin(2), rst=Pin(4), width=480, height=320)
# tft.fill(0)
# run(tft)