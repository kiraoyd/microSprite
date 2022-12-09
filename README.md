# microSprite

A Sprite library developed in MicroPython for the Micro:bit computer. Micropython code runs exclusively in the Micropython editing environment for the Micro:bit hardware.

A Sprite is represented by a single LED on the Microbit's 25 LED display board. This library contains functionality for controlling the position and movment of a Sprite on the Microbit, by controlling which LED lights up to represent the Sprite at any given time. This library includes options to help control how the Sprite interacts with other "objects" displayed to the LED screen, as well as the borders of the LED display itself. It also provides support for the creation and control of a grouping of single Sprites that acts as one.

To run code from this repo, copy the files into the Micro:bit online Python Editor that can be found here:

https://python.microbit.org/v/3/api/microbit.display

To run, click the "simulator" button at the top right hand side of the browser. This will run the code on a virtual Micro:bit, which displays to the browser window.

Note that this library uses calls to the Micropython sleep() function, which operates slightly differently from Pythons sleep() function. Micropython's sleep() function takes the argument in milliseconds, whereas Pythons takes it in seconds.

As of 12/8/2022:

We are still working on connecting the microPython source code to VSCode to test on our local machines.
The repo for the source code is:
https://github.com/bbcmicrobit/micropython/blob/master/README.md
