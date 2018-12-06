'''
  This is doc string
'''
class Car:
  '''
    This is a Car class representing real world object
  '''
  counter = 0
  # To share variable among the objects, make variable of class not object
  def __init__(self, name, model=2018):
    self.name = name
    self.model = model
    self.status = 'Stop'
    self.type= None
    Car.counter += 1
    
  def start(self):
    '''
      Change status to start
    '''
    self.status = 'Start'
    
  def stop(self):
    '''
      Change status to stop
    '''
    self.status = 'Stop'
    
c = Car('Honda')
c.start()
# print('C counter', c.counter)
# print(c.__dict__)
b = Car('Hyundai')
# print('B counter', b.counter)
# print(b.__dict__)
# print(Car.__dict__)


c.counter = 3 # This takes counter as its own instance and it destroys the link between the class and object for same attribute
Car.counter += 5 # Change the variable value of class object
print(b.counter)
print(c.counter)

# Note: Don't change class object property from instance. Change using class. 