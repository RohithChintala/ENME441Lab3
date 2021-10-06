from PCF8591 import PCF8591

class Joystick:
  def __init__(self, address):
    self.pcf8591 = PCF8591( address)
    def getX():
      #self.p =  adc.address
      return(self.pcf8591.read(0))
    def getY():
      #self.q = adc.address
      return(self.pcf8591.read(1))


try:
  while 1:
    J = Joystick( 0x48)
    print(J.getX())
    sleep(0.5)
    print(J.getY())
    sleep(0.5)
except KeyboardInterrupt:
 print('\nExiting')