import PCF8591

class Joystick:
  def __init__(self, bus, address, p, q):
    self.adc = PCF8591(bus, address)
    def getX():
      self.p =  adc.address
      return(self.PCF8591.read(0))
    def getY():
      self.q = adc.addre
      return(self.PCF8591.read(1))


try:
  while 1:
    J = Joystick(1, 0x48)
    print(J.getX())
    sleep(0.5)
    print(J.getY())
    sleep(0.5)
except KeyboardInterrupt:
 print('\nExiting')