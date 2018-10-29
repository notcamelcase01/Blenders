# Blenders
Project Multicolor 3D printing

## Decoder
Code arduino to run stepper accordingly <br>
File name : [decoder.py](https://github.com/amangautam015/Blenders/blob/master/decoder.py "Decoder")  [Click Here](https://github.com/amangautam015/Blenders/blob/master/decoder.py "Decoder")<br>
Libraries used : <br>
- numpy `pip install numpy`
- PIL `pip install Pillow`
- pyfirmata `pip install pyfirmata`
- scipy `pip install scipy`


Input :  A single color gray image<br>
Output : Two stepper motor extruding PFA (black and white) at speeds to give the input grayscale variation

#### Variable Definations
- resolution : how close to input gray image // high resolution increases voxel length is not good
- min_speed :  actually mimumum time delay for nema17 stepper nothing related to speed
- step : array of white and black step number

## Function Definations

**def create_image**

Creates a test image **not required** to be runed just download image fomr this [link](https://raw.githubusercontent.com/amangautam015/Blenders/master/final_result.png") and save it in same directory of python file(decoder.py)

---

**def get_intensity**

Fetchs gray scale intensity of image assumme image to be mono-colored for testing purpose just imput required gray scale intensities in `color_grad` variable at line `136` of decoder.py

---

**def motor_white / def motor2_black**

Takes **N** number of steps to be executed as variable and runs the stepper for **N** times

**def step_genertor**
For a ceertain gray value we figure out how many steps should black/white motor runs say W,B <br>
Divide W,B as sum of `W = w 1+ w 2+ w 3 ....` and similarly for black<br>
For  particular gray scale returns an array of which have reduced number steps in format `[[w 1,b 1],[w 2,b 2]........]` where w,b correspind to white and black .<br>
```
White stepper runs w 1 steps
Black runs b 1 steps
again
White runs w 2 steps
Black runs b 2
goes on .............
```
<br>
This is better than running every step for white or black runned in single go

---

**def pixel**
Same as step_generator just cares of edge cases and gives final array of steps required to print one voxcel

---

**def printer**
Actuates motor and start printing . Receives one array needed to print a voxcel

---

> Arduino Uno
