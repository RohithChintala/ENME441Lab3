from PCF8591 import PCF8591
from time import sleep
import smbus

''''
class PCF8591:

  def __init__(self,address):
    self.bus = smbus.SMBus(1)
    self.address = address

  def read(self,chn): #channel
      try:
          self.bus.write_byte(self.address, 0x40 | chn)  # 01000000
          self.bus.read_byte(self.address) # dummy read to start conversion
      except Exception as e:
          print ("Address: %s \n%s" % (self.address,e))
      return self.bus.read_byte(self.address)

  def write(self,val):
      try:
          self.bus.write_byte_data(self.address, 0x40, int(val))
      except Exception as e:
          print ("Error: Device address: 0x%2X \n%s" % (self.address,e))
'''
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
    print(J.getX(), J.getY())
    sleep(0.5)
except KeyboardInterrupt:
 print('\nExiting')