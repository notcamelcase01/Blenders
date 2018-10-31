from PIL import Image
import numpy as np
from pyfirmata import Arduino, util
import sys
import time
from scipy.interpolate import interp1d

'''
Inilization look line 140 for different color pixel
'''
resolution = 255
stepPin_white = 6
dirPin_white = 7
stepPin2_black = 3
dirPin2_black = 4

min_speed = 0.013
'''
Created an grayscale image of intensity 128 (0-255) for calabration of motor speed
'''

def create_image():
    k = Image.open('result.png')
    size = (40,40)
    width, height = size
    k = k.resize((round(width/4),round(height/4)))
    out = Image.new('L', k.size)


    for x in range(round(width/4)):
        for y in range(round(height/4)):
            out.putpixel((x,y),128)
    out.save('final_result.png')

'''
Gets image color (here gray scale intensity )
'''
def get_intensity():
    k = Image.open('final_result.png').getcolors()
    print(k)
    print(k[0][1])
    return (k[0][1])

white_length = 0
black_length = 0

def motor_white(step_local):
   global white_length
   board.digital[dirPin_white].write(1)
   for i in range(0,step_local):
       board.digital[stepPin_white].write(1)
       time.sleep(min_speed)
       board.digital[stepPin_white].write(0)
       time.sleep(min_speed)
       white_length = white_length + 1

def motor2_black(step_local):
    global black_length
    board.digital[dirPin2_black].write(1)
    for i in range(0, step_local):
        board.digital[stepPin2_black].write(1)
        time.sleep(min_speed)
        board.digital[stepPin2_black].write(0)
        time.sleep(min_speed)
        black_length = black_length +1

f = 1.8/180

'''
Resolved Step function 
'''

def step_generator(w,b):
    x = w / b
    y = 1
    if x < 1:
        x = 1 / x
    if (x <= 1.2 or x >= 1.8) and (x<=2.3 or x>=2.7) and (x<=3.3 or x>=3.6):
        x = round(x)
        y = 1
    elif x > 1.4 and x <= 1.6:
        y = 2
        x = round(y * x)
    else:
        y = 3
        x = round(y * x)

    step = []

    if w < b:
        d = int(min(w // y, b // x))
        for i in range(0, d):
            step.append([x, y])

            w = w - y
            b = b - x
        step.append([w, b])

    elif w == b:
        step = [[1, 1]] * w

    else:
        d = int(min(w // x, b // y))
        for i in range(0, d):
            step.append([x, y])
            w = w - x
            b = b - y
        step.append([w, b])
    return step


def pixel(color_grad):
    w = int(mwhite(color_grad))
    b = int(mblack(color_grad))
    print([w, b])
    if w != 0 and b != 0:
        step = step_generator(w, b)
    else:  # Handling edge cases
        if w == 0:
            step = [[0, 1]]*resolution
            delay = 0.16
        else:
            step = [[1, 0]]*resolution
            delay = 0.16

    return step


def printer(step):
    try:
        for kk in range(0,1):
            for i in step:
                motor2_black(i[1])
                motor_white(i[0])
                time.sleep(delay)
    except KeyboardInterrupt:
        print("KeyInterrupt")
        pass
delay = 0.36
color_grad = [200]*3 #+[128]*10+[0]*5 #gray scale intensity replace constant from get_intensity funciton



'''
Speed of Stepper according to color required
'''
mwhite = interp1d([0,255],[0,resolution])  #Linear plotting
mblack = interp1d([0,255],[resolution,0])

board = Arduino("COM5")
it = util.Iterator(board)
it.start()
voxel=1
time.sleep(10)
for color in color_grad:
    step = pixel(color)
    print("step [white,black] : " + str(step))
    print(len(step))
    printer(step)
    print("White length excruded :" + str(f * white_length) + "mm\n" + "Black Length excruded :" + str(
        f * black_length) + 'mm')
    white_length = 0
    black_length = 0
    print("Voxel : " + str(voxel))
    voxel = voxel+1


print("----------------------")