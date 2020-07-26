# Blenders :rainbow:
Project Multicolor 3D printing

### Problem Statement
- 3D Printed products are usually monotonous in colour
- Inability to print object in a variety of colours in the same build
- Enable products to closely emulate the original and make it consumer friendly

### Prototype Overview
- To provide a proof of concept of mixing of heated filaments in the extruder to achieve varying grayscale outputs
- To show that multicolour 3d printing can be achieved at much lesser cost than that is commercially available

### Control Algorithm and Code Implementation

## Mixer
Code arduino to run stepper accordingly <br>
File name : [decoder.py](https://github.com/amangautam015/Blenders/blob/master/decoder.py "Decoder")  [:link:](https://github.com/amangautam015/Blenders/blob/master/decoder.py "Decoder")<br>
Libraries used : <br>
- numpy `pip install numpy`
- PIL `pip install Pillow`
- pyfirmata `pip install pyfirmata`
- scipy `pip install scipy`


Input :  A single color gray image or gray intensity (0-255) <br>
Output : Two stepper motor extruding PLA (black and white) at speeds to give the input grayscale variation

#### Variable Definations [:link:](https://github.com/amangautam015/Blenders/blob/41a512766da2fcb77d7b0aa4f80fc1331032ceb6/decoder.py#L11)
- resolution : how close to input gray image // high resolution increases voxel length is not good
- min_speed :  maximum time delay for nema17 stepper motor maximum time delay minimum speed 
- step : array of white and black step number

## Function Definations

**def create_image** [:link:](https://github.com/amangautam015/Blenders/blob/41a512766da2fcb77d7b0aa4f80fc1331032ceb6/decoder.py#L22)

Creates a test image **not required** to be executed download image from this [link](https://raw.githubusercontent.com/amangautam015/Blenders/master/final_result.png") and save it in same directory of python file(decoder.py)

---

**def get_intensity** [:link:](https://github.com/amangautam015/Blenders/blob/41a512766da2fcb77d7b0aa4f80fc1331032ceb6/decoder.py#L38)

Fetchs gray scale intensity of image assumme image to be mono-colored for testing purpose just input required gray scale intensities in `color_grad` variable at [`At line 140 of decoder.py`](https://github.com/amangautam015/Blenders/blob/41a512766da2fcb77d7b0aa4f80fc1331032ceb6/decoder.py#L140) . `color_grad` is an array containing different voxel color informtion for one voxel just input one item in list `color_grad = [200]`<br>
For Example <br>
```
color_grad = [0]*10 + [128]*5 + [200]*1 
This will print out 10 voxel of gray intensity 0 , 5 of 128 and 1 of 200
```

---

**def motor_white / def motor2_black** [:link:](https://github.com/amangautam015/Blenders/blob/41a512766da2fcb77d7b0aa4f80fc1331032ceb6/decoder.py#L47)

Takes **N** number of steps to be executed as variable and runs the stepper for **N** times

---

**def step_genertor** [:link:](https://github.com/amangautam015/Blenders/blob/41a512766da2fcb77d7b0aa4f80fc1331032ceb6/decoder.py#L73)

For a certain gray value we figure out how many steps should black/white motor runs say W,B <br>
Divide W,B as sum of `W = w 1+ w 2+ w 3 ....` and similarly for black<br>
For  particular gray scale returns an array of which have reduced number steps in format `[[w 1,b 1],[w 2,b 2]........]` where w,b correspond to white and black .<br>
```
White stepper runs w 1 steps
Black runs b 1 steps
again
White runs w 2 steps
Black runs b 2
goes on .............
```

---

**def pixel** [:link:](https://github.com/amangautam015/Blenders/blob/41a512766da2fcb77d7b0aa4f80fc1331032ceb6/decoder.py#L112)

Same as step_generator just cares of edge cases and gives final array of steps required to print one voxel

---

**def printer** [:link:](https://github.com/amangautam015/Blenders/blob/41a512766da2fcb77d7b0aa4f80fc1331032ceb6/decoder.py#L129)

Actuates motor and start printing . Receives one array needed to print a voxel

---

## Run the project  
- Install Python 3.6(Python3.+ would work) and pip [Check Here for installation](https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation) 
- [Download project](https://github.com/amangautam015/Blenders/archive/master.zip)
- Open cmd in project directory
`Blenders>pip install virtualenv`<br>
`Blenders>cd venv/Scripts`<br>
`Blenders/venv/Scripts>activate.bat`<br>
`Blenders/venv/Scripts>cd ..`<br>
`Blenders>python decoder.py` 
 Run this command while you are connected to arduino uno check port by default its `COM5` in [`decoder.py line 150`](https://github.com/amangautam015/Blenders/blob/41a512766da2fcb77d7b0aa4f80fc1331032ceb6/decoder.py#L150) change it as in your System
 
 ---

> Arduino Uno

## Contributers
- Ravindra Sagar ( BTech ME , IITB )
- Nishant Venkatesh ( BTech ME , IITB )
- Sujeet Singh ( BTech ME , IITB )
- Prakhar Joshi ( BTech ME , IITB )
- Maurya Patel ( BTech ME , IITB )
- Sheryas Bhatt ( BTech ME , IITB )
- Himanshu Singh ( BTech ME , IITB )
- Aman Gautam ( BTech ME , IITB )
