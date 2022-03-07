class Weapon(object):
  _name = str()
  _capacity = int()
  _power = int()
  
  def __init__(self, name, capacity, power) -> None:
    self._name = name
    self._capacity = capacity
    self._power = power