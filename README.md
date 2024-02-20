# Circuit-Cube-Python
(Somewhat) Beginner friendly Python code for controlling a LEGO circuit cube via Bluetooth (LE)

# Usage:
## Dependencies
For the project to work, bleak is required. Install it via pip using `$ pip install bleak` or get it from github:
https://github.com/hbldh/bleak
## Pairing your device with your cube
Note that when I used this code, I first added the circuit cube as a known device in my bluetooth settings (using Windows 10). I have not tested whether this code works without this step, or how this step may work on other devices.
## Getting your cube's ID
To get the unique BLE address for your circuit cube (for use in connecting), navigate to the "code" directory and run `find_device.py`. Make sure your circuit cube is in bluetooth mode. The program should print out a list of nearby devices. The program will print the device address and the device name. The circuit cube may be named something like "Tenka Cube". The address can be used to connect to the cube.
## Connecting to the cube
I would recommend writing your own code for connecting and controlling the cube, but to help with this I have left some example files in the "code" directory. These should be pretty well commented, so understanding the cube's communication shouldn't be too difficult
## Additional resources
Since when I coded this, I had no knowledge of how to do bluetooth with Python I had to learn a lot. Once I found bleak, which actually worked for the BLE I needed to do, I had to learn how BLE communication works. I had to learn what GATT was (https://learn.adafruit.com/introduction-to-bluetooth-low-energy/gatt) and how to use it (which I did by looking through the bleak source code) (https://github.com/hbldh/bleak). I also learned how to connect to the circuit cube through the only other project I could find. (https://github.com/asperka/LEGORemoteCircuitCube). If you find yourself stuck, or need some more info these are some good places to look.
