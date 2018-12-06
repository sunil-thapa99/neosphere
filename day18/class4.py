'''
  This is doc string
'''
class Car:
  def __init__(self, name, model=2018):
    self.name = name
    self.model = model
    self.status = 'Stop'
    self.type= None
    
  def _start(self): # Protected
    self.status = 'Start'
    
  def __stop(self): # Private
    self.status = 'Stop'
  @staticmethod
  def r(d):
    return d/2
    
c = Car('Honda')
c._start()
print(c.__dict__)
dir(c)
c._Car__stop()
print(c.__dict__)
b = Car('Hyundai')

