# Circuit-Cube-Python
Python code for connecting via BLE to a LEGO Circuit Cube

# Usage:
## Dependencies
For the project to work, bleak is required. Install it via pip using `$ pip install bleak` or get it from github:
https://github.com/hbldh/bleak
## Pairing your device with your cube
Note that when I used this code, I first added the circuit cube as a known device in my bluetooth settings (using Windows 10). I have not tested whether this code works without this step, or how this step may work on other devices.
## Getting your cube's ID
To get the unique BLE address for your circuit cube (for use in connecting), navigate to the "code" directory and run `find_device.py`. Make sure your circuit cube is in bluetooth mode. The program should print out a list of nearby devices. The program will print the device address and the device name. The circuit cube may be named something like "Tenka Cube". The address can be used to connect to the cube.
## Connecting to the cube
I would reccommend writing your own code for connecting and controlling the cube, but to help with this I have left some example files in the "code" directory. These should be pretty well commented, so understanding the cube's communication shouldn't be too difficult
