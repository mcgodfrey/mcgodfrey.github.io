---
title: 'Servo Motor Control with Mojo FPGA board'
date: '2016-03-06T07:01:55+00:00'
author: matt
layout: post
permalink: /2016/03/06/servo-motor-control-with-mojo-fpga-board/
image: /img/2016/03/img_20160306_173311_11-1200x900.jpg
categories:
    - Projects
tags:
    - FPGA
    - Mojo
    - Verilog
---

This post is part of my series on building a kinetic sculpture with the Mojo FPGA development board. ([Part1](http://dangerfromdeer.com/2016/01/09/mojo-fpga-development-board/) Part2).

My [Mojo development board ](https://embeddedmicro.com/products/mojo-v3.html) finally turned up and so I've been playing around with it for the last week. 
This post is just a quick update of some fist test code to control some servo motors and sweep them back and forth. The end goal of this project is full independent control of multiple servos to create moving sculptures. See [this ](http://dangerfromdeer.com/2016/01/09/mojo-fpga-development-board/) post for an overview of the project. 

For this first stage, I want to simply sweep a few sevos back and forth through their full range at different speeds. I will be using Verilog for the project (since all of the Mojo example code is written in Verilog) and the [mojo-base-project](https://github.com/embmicro/mojo-base-project) as a starting point. There are also some [tutorials](https://embeddedmicro.com/tutorials/mojo) and example code on the Mojo website for counters and servo control which I have based a lot of this code on.

![Demo servo motor control with Mojo FPGA board.](/img/2016/03/servo_motor_demo.gif)

So, jumping straight in, download the code [here](https://github.com/mcgodfrey/kinetic_sculpture/releases/tag/v0.1) and I’ll go through how it works below.

## How it works

There are 2 basic modules in this example.

- An 8-bit up-down counter which generates the positions for each motor
- The servo controller itself which translates the 8-bit position into a PWM signal that the servo motor expects.

The main top level module code is very simple. It uses generate loops to create an up-down counter for each servo, and a corresponding servo-controller module. The period of the timer is different for each loop, determined by the CTR_LEN parameter which is varied for each one. The relevant code is shown below.

[https://gist.github.com/mcgodfrey/10efe8f8644f3a7c190e]

## Servo Controller

The servo controller is almost identical to the tutorial code on the mojo [website](https://embeddedmicro.com/tutorials/mojo/servos).
I have plans to update it and make the timing a bit more precise (it currently overshoots the endpoints and so there is some clipping in the position at either end) but it is working well enough for testing purposes as is.

The servo output is a modified PWM signal with a period of ~20ms (the exact period isn’t too important apparently) and a pulse width which determines the position. Full range is 1ms -> 2ms, with 1.5ms being the centre position. The Mojo runs at 50MHz, so to get a 50Hz PWM frequency (50Hz -> 20ms period) we need a 20 bit counter (2^20 = 1,048,576).

Then, within each 20ms period (~1,000,000 values) the full range of 1ms-2ms corresponds to counter values of 50,000 – 100,000. So we need an offset and a scaling factor. The mojo tutorial uses a scaling factor of 256 (the actual value is 50,000/255=196 which is “close enough”) and an offset of 165. This approximate scaling gives the correct centre value for 1.5ms, but the 2 end points will be slightly wrong. This is ok for now, but will need to be improved upon later once I need some finer position control.

The code below just creates a 20 bit counter and compares the counter value to the position input once it has been offset and scaled as described above. It then sets the output to 0 or 1 depending on the value of counter.

[https://gist.github.com/mcgodfrey/b94acfc796c240a4a164]

## Next Step

Now that I can control the servo positions, the next step is to be able to save a list of positions somewhere so that I can pre-program in movements to create the 3D sculptures.

My original plan was to use the AVR microcontroller on the Mojo board to handle this and just send the new positions to the FPGA. However, there is not enough memory in the AVR to store any reasonable amount of movement data so I will need some form of external memory. I figure if I need external memory anyway, I may as well do the whole thing in the FPGA. I have some 512kb i2c EEPROMs lying around so I am thinking they could do the job. The plan is to pre-load the position data onto one of them and then the FPGA will just read the data and update the servo positions accordingly.

However, this means that I need my FPGA to speak i2c! A quick search hasn’t revealed much Verilog code for this so I decided (possibly foolishly) to write my own i2c master module. This will be a good test of my verilog and FPGA skills in general (which were basically non-existent a fortnight ago) and hopefully a useful learning experience. The current status is that the i2c module and a wrapper module to communicate and read from the EEPROM are written and seem to work in the simulator. I’ve loaded it onto the board to test (where it didn’t magically work on the first try. Who would have thought?) but haven’t had a chance to do any testing or debugging yet.

Stay tuned for an update once I get the next stage working.
