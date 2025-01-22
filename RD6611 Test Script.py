import serial
from time import sleep
import os
x = 1

num = input("What number is the COM Port?\n")
port = 'COM' + num
ser = serial.Serial(port, 38400, timeout = 3)
os.system('cls')

while x == 1:
    print("Running on port " + port)
    print("Setting Auto Source to 'Off'")
    ser.write([0xAA, 0x54, 0x00, 0x00, 0xFE])
    sleep(3)
    print("Setting Source to 'HDMI'")
    ser.write([0xAA, 0x69, 0x00, 0x03, 0xC0])
    sleep(8)
    print("Setting Backlight to 100")
    ser.write([0xAA, 0x1B, 0x00, 0x64, 0xD5])
    sleep(5)
    print("Setting Backlight to 10")
    ser.write([0xAA, 0x1B, 0x00, 0x0A, 0xBB])
    sleep(5)
    print("Setting Backlight to 50")
    ser.write([0xAA, 0x1B, 0x00, 0x33, 0x82])
    print("Done!")
    sleep(3)
    os.system('cls')
    end = input("Would you like to test another unit? (y/n)\n")
    if end == "y":
        os.system('cls')
    elif end == "n":
        x = 0