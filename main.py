from PCF8591 import PCF8591
from time import sleep
import smbus

class Joystick:
  def __init__(self, address):
    self.adc = PCF8591(address)
  def getX(self):
    return(self.adc.read(0))
  def getY(self):
    return(self.adc.read(1))


try:
  while 1:
    J = Joystick(0x48)
    #print(J.getX(), J.getY())
    #print('%d, %d' % (J.getX(),J.getY()))
    print("{:-^10}|{:<>15}".format(J.getX(), J.getY()))
    sleep(0.1)
except KeyboardInterrupt:
 print('\nExiting')