from PIL import Image
import numpy as np
from pyfirmata import Arduino, util
import sys
import time


'''
Created an grayscale image of intensity 128 (0-255) for calabration of motor speed
'''




stepPin_white = 6
dirPin_white = 7
stepPin2_black = 3
dirPin2_black = 4
stepSize = 1



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






white_length = 0
black_length = 0

def motor_white():
   global white_length
   board.digital[dirPin_white].write(1)
   for i in range(0,stepSize):
       board.digital[stepPin_white].write(1)
       time.sleep(0.015500)
       board.digital[stepPin_white].write(0)
       time.sleep(0.015500)
       white_length = white_length + 1





def motor2_black():
    global black_length
    board.digital[dirPin2_black].write(0)
    for i in range(0, stepSize):
        board.digital[stepPin2_black].write(1)
        time.sleep(0.015500)
        board.digital[stepPin2_black].write(0)
        time.sleep(0.015500)
        black_length = black_length +1

f = 1.8/180
board = Arduino("COM5")
it = util.Iterator(board)
it.start()
try:
    while 1:
        motor2_black()
        motor_white()
except KeyboardInterrupt:
    print("White length excruded :" + str(f*white_length)+"mm\n"+"Black Length excruded :" +str(f*black_length)+'mm')
    pass

print("----------------------")