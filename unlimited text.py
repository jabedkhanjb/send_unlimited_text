import pyautogui as jb
import time

message = input("Enter a message: ")
limit = input("Enter the message limitation: ")
count = 0

time.sleep(2)
while count < int(limit):
    jb.typewrite(message)
    jb.press("Enter")
    count += 1 #by commenting this line we can print unlimited message
