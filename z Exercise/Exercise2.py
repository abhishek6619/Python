#Good Morning sir
# Create a python program capable of greeting you with Good Morning,
# Good Afternoon and Good Evening. your program should use time module
# to get the current hour. Here is a Sample program and documentation link for you
# https://docs.python.org/3/library/time.html#time.timestrf

import time
name = input("Enter your name: ")

hour = int(time.strftime('%H'))
if (hour >= 4 and hour < 12):
    print("Good Morning", name)
elif (hour >= 12 and hour < 16):
    print("Good Afternoon", name)
elif (hour >= 16 and hour <= 18):
    print("Good evening", name)
else:
    print("Good night", name)