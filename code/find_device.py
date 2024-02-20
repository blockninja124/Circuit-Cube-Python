import asyncio
from bleak import BleakScanner

async def main():
    devices = await BleakScanner.discover() #find all nearby devices
    if devices == []:
        print("No devices found. Check that your bluetooth is enabled.")
    else:
        print("Devices found:")
    for d in devices:
        print(d)
asyncio.run(main())
