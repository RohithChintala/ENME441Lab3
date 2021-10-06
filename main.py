from PCF8591 import PCF8591
from time import sleep

class Joystick:
  def __init__(self, address):
    self.adc = PCF8591(address)
  def getX():
    return(self.PCF8591.read(0))
  def getY():
    return(self.PCF8591.read(1))


try:
  while 1:
    J = Joystick(0x48)
    print(J.getX)
    sleep(0.5)
    print(J.getY)
    sleep(0.5)
except KeyboardInterrupt:
 print('\nExiting')