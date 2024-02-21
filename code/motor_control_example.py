import asyncio
from bleak import BleakClient

CIRCUIT_CUBE_SERVICE_UUID = "6e400001-b5a3-f393-e0a9-e50e24dcca9e" # DONT CHANGE THESE! 
CIRCUIT_CUBE_TX_CHRACTERISITCS_UUID = "6e400002-b5a3-f393-e0a9-e50e24dcca9e" # These are linked to the Cubes hardware, 
CIRCUIT_CUBE_RX_CHRACTERISITCS_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e" # and are the same for all cubes. (I believe)


def build_velocity_command(channel, velocity): # function for creating the neccesary string for talking to the cube
    sign = "-" if velocity < 0 else "+" 
    value = 0 if velocity == 0 else (55 + abs(velocity))
    cmd = f"{sign}{value:03}{chr(ord('a') + channel)}" # final string should be {+/-}{0/55+abs(vel) (3 char long)}{unicode char( unicode num(a) + channel )}
    return cmd

def all_motors(vel1, vel2, vel3): # the cube also understands multiple velocity commands together. Here it just combines 3 (1 for each motor)
    command = build_velocity_command(0, vel1) + build_velocity_command(1, vel2) + build_velocity_command(2, vel3)
    return command
    

address = "FC:58:FA:CF:3C:6A" # My circuit cube address. Make sure to replace with your own!


    
async def main():

    print("Establishing initial connection...")

    async with BleakClient(address) as client: # connect to cube
        t = await client.get_services() # get GATT services
        tx = t.get_characteristic(CIRCUIT_CUBE_TX_CHRACTERISITCS_UUID) # get the GATT service's GATT characteristic of the tx UUID
        rx = t.get_characteristic(CIRCUIT_CUBE_RX_CHRACTERISITCS_UUID) # get the GATT service's GATT characteristic of the rx UUID
        
        print("Enter speed for each motor with spaces seperating each. e.g. '1 1 1'. To exit, enter break")
        while True:
            speed = input("Enter speed: ")
            if speed == "break":
                break
            speed = speed.split(" ") # split speed into (hopefully) 3 numbers (in str form)

            for index, i in enumerate(speed):
                speed[index] = int(i) # convert each item from a str number to an actual int
                
            await client.write_gatt_char(tx, all_motors(speed[0],speed[1],speed[2]).encode()) # Actually transmitting. Uses tx to talk to (rx is for recieving). 
                                                                                              # It then uses our 'all_motors' func to build the correct command string.
                                                                                              # This then has to be encoded into bytes for transmision.
    
asyncio.run(main())
