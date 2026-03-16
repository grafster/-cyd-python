# Drawing function cheat sheet
    def rect(self,x,y,w,h,color,fill=False):
        print ('rect {x},{y},{w},{h},{color}')
    def circle(self, x, y, radius, color, fill=False):
        print('circle')
    def line(self, x0, y0, x1, y1, color):
        print(f'line {x0} {y0} {x1} {y1}')
    def triangle(self, x0, y0, x1, y1, x2, y2, color, fill=False):
        print('triangle')
    def color(self, x,y,z):
        print(f'color {x} {y} {z}')
        return 1
    def colour(self, x,y,z):
        print(f'color {x} {y} {z}')
        return 1
    def pixel(self,x,y,color):
        print(f'pixel {x} {y} {color}')
    def fill(self, color):
        print('fill')
    def text(self,x,y,txt,fgcolor,bgcolor):
        print ('text ' + txt)
    def upscaled_text(self,x,y,txt,fgcolor,*,bgcolor=None,upscaling=2):
        print('upscaled text ' + txt)
    def image(self,x,y,filename):
        print('image')

## Display X & Y Co-ordinates

The display is 480 pixels wide and 320 high

x = 0, y = 0 is the top left of the screen
x = 480, y = 320 is the bottom right of the screen

## Colours

display.colour(r, g, b)

r = Red 0-255 
g = Green 0-255 
b = Blue 0-255

### Example

red = display.colour(255,0,0)

## Set a single pixel

display.pixel(x, y, colour)

x = screen x
y = screen y
colour = colour for pixel

### Example

#Set central pixel white
display.pixel(240,160, display.colour(255,255,255))


# Text

display.text

# Circles 


# Rectangles
