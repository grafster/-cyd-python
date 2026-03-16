# Drawing function cheat sheet

## Display X & Y Co-ordinates

The display is 480 pixels wide and 320 high

x = 0, y = 0 is the top left of the screen
x = 480, y = 320 is the bottom right of the screen

## Colours

display.colour(r, g, b)

| Parameter | Description |
| --- | --- |
|r | Red 0-255 |
|g | Green 0-255 |
|b | Blue 0-255 |

### Example

red = display.colour(255,0,0)

## Set a single pixel

display.pixel(x, y, colour)

| Parameter | Description |
| --- | --- |
| x | screen x |
| y | screen y |
| colour | colour for pixel |

### Example

#Set central pixel white

display.pixel(240,160, display.colour(255,255,255))

# Fill screen with a single colour 

display.fill(color)

| Parameter | Description |
| --- | --- |
| colour | colour for screen |

### Example

#Set whole screen white

display.fill(display.colour(255,255,255))

# Draw an image from the disk

display.image(x, y, filename)

| Parameter | Description |
| --- | --- |
| x | screen x position to display image|
| y | screen y position to display image |
| filename | image file (currently only logo.565 |

### Example

#Draw scout logo at top left of screen

display.image(0, 0, 'logo.565')

# Text

display.text(x,y,txt,fgcolor,bgcolor)

| Parameter | Description |
| --- | --- |
| x | screen x position to display text |
| y | screen y position to display text |
| txt | the text to display |
| fgcolour | the foreground colour for the text |
| bgcolour | the background colour for the text |

### Example

#draw 'hello' with white text on black background
display.text(10,295, 'hello', display.color(255,255,255), display.color(0,0,0))

# Large text

    def upscaled_text(self,x,y,txt,fgcolor,*,bgcolor=None,upscaling=2):
        print('upscaled text ' + txt)
| Parameter | Description |
| --- | --- |
|r | Red 0-255 |
|g | Green 0-255 |
|b | Blue 0-255 |

### Example

red = display.colour(255,0,0)

# Circles 

    def circle(self, x, y, radius, color, fill=False):
        print('circle')

| Parameter | Description |
| --- | --- |
|r | Red 0-255 |
|g | Green 0-255 |
|b | Blue 0-255 |

### Example

red = display.colour(255,0,0)
# Rectangles

    def rect(self,x,y,w,h,color,fill=False):
        print ('rect {x},{y},{w},{h},{color}')
| Parameter | Description |
| --- | --- |
|r | Red 0-255 |
|g | Green 0-255 |
|b | Blue 0-255 |

### Example

red = display.colour(255,0,0)

# Line
    def line(self, x0, y0, x1, y1, color):
        print(f'line {x0} {y0} {x1} {y1}')

| Parameter | Description |
| --- | --- |
|r | Red 0-255 |
|g | Green 0-255 |
|b | Blue 0-255 |

### Example

red = display.colour(255,0,0)

# Tringle

    def triangle(self, x0, y0, x1, y1, x2, y2, color, fill=False):
        print('triangle')

| Parameter | Description |
| --- | --- |
|r | Red 0-255 |
|g | Green 0-255 |
|b | Blue 0-255 |

### Example

red = display.colour(255,0,0)
