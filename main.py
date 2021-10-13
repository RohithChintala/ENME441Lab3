from PCF8591 import PCF8591 #imports PCF8591 class
from time import sleep #imports sleep
#import smbus

class Joystick: #creates joystick class
  def __init__(self, address): #instantiates address 
    self.adc = PCF8591(address) #calls PCF8591 class by composition
  def getX(self): #creates class method
    return(self.adc.read(0)) #returns adc read of address 0
  def getY(self): #creates class method
    return(self.adc.read(1)) #returns adc read of address 0


try: #runs if no error
  while 1: #runs infinite loop
    J = Joystick(0x48) #creates J object from joystick class
    print("{:>3}, {:>3}".format(J.getX(), J.getY())) 
    #prints X and Y values in proper format
    sleep(0.1) # sleeps for 100 ms
except KeyboardInterrupt: #ends code with keyboard interupt
 print('\nExiting')