import PCF8591

class Joystick:
  def __init__(self, bus, address):
    self.adc = PCF8591(bus, address)
    def getX():
      return(self.adc.read(0))
    def getY():
      return(self.adc.read(1))


try:
  while 1:
    J = Joystick(1, 0x48)
    print(J.getX())
    sleep(0.5)
    print(J.getY())
    sleep(0.5)
except KeyboardInterrupt:
 print('\nExiting')