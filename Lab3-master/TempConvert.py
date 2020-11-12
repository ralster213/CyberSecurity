#TempConvert.py
#Name:
#Date:
#Assignment:

from time import sleep

def main():
    #Prompt the user for a Fahrenheit temperature
    (tempF) = input("Type in a temperature in degrees Fahrenheit: ")
    #Convert that temperature to celsius, rounding to 1 decimal percision
    tempC = ((float(tempF)-32) *5/9 )
    sleep(1)
    print(round(tempC, 1))
    #Output converted temperature.

main()
