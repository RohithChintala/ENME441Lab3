#   To check address: sudo i2cdetect -y 1

import PCF8591

class Joystick:
  def __init__(self,bus,address):
    self.adc = PCF8591(bus, address)
    def getX():
      return(read(0))
    def getY():
      return(read(1))

J = Joystick()
print(J.getX())
sleep(0.5)
print(J.getY())
sleep(0.5)