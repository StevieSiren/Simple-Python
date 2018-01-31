'''Temperature Converter
Author: @StevieSiren
'''
# Need this to exit program
import sys

start = input("Press 'f' to convert F to C, or press 'c' to convert C to F")

def fahr_to_cels():
    x = int(input('Enter your degrees F: '))
    cels = (x - 32) / 1.8
    print('{} degrees fahrenheit is {} celsius'.format(x, cels))

def cels_to_fahr():
    x = int(input("Enter your degrees C: "))
    fahr = x * 1.8 + 32
    print('{} degrees celsius is {} fahrenheit'.format(x, fahr))

while True:
    if start == 'f':
        fahr_to_cels()
    elif start == 'c':
        cels_to_fahr()
    else:
        print('Please select either "f" or "c".')

    restart = input("Press 'r' to restart, or press 'q' to quit.")
    if restart == 'r':
        start = input("Press 'f' to convert F to C, or press 'c' to convert C to F")
    elif restart == 'q':
        sys.exit()
