import asyncio
from bleak import BleakClient
import time

CIRCUIT_CUBE_SERVICE_UUID = "6e400001-b5a3-f393-e0a9-e50e24dcca9e"
CIRCUIT_CUBE_TX_CHRACTERISITCS_UUID = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"
CIRCUIT_CUBE_RX_CHRACTERISITCS_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"


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

        while True:
            instructions = input("enter instructions: ")
            print("running...")
            for letter in instructions:
                if letter == "w":
                    await client.write_gatt_char(tx, all_motors(50, 0, 50).encode()) # Actually transmitting. Uses tx to talk to (rx is for recieving). 
                                                                                     # It then uses our 'all_motors' func to build the correct command string.
                                                                                     # This then has to be encoded into bytes for transmision.
                    time.sleep(1)
                    await client.write_gatt_char(tx, all_motors(0, 0, 0).encode())   # motors once told what to do, will continue spinning at that speed until 
                                                                                     #told to stop. Make sure to send a 0 0 0 signal when finished
                
                elif letter == "s":
                    await client.write_gatt_char(tx, all_motors(-50, 0, -50).encode()) # negative speeds spin the other direction
                    time.sleep(1)
                    await client.write_gatt_char(tx, all_motors(0, 0, 0).encode())
                
                elif letter == "a":
                    await client.write_gatt_char(tx, all_motors(50, 0, -50).encode())
                    time.sleep(0.45)
                    await client.write_gatt_char(tx, all_motors(0, 0, 0).encode())
                
                elif letter == "d":
                    await client.write_gatt_char(tx, all_motors(-50, 0, 50).encode())
                    time.sleep(0.45)
                    await client.write_gatt_char(tx, all_motors(0, 0, 0).encode())
    
asyncio.run(main())