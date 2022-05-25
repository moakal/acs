# animals task
# 25/05/2022

class Animal:
  def __init__(self):
    self.animalSpecies = 'unknown'
    self.age = 0
    self.threatLevel = 'peaceful'
    self.hungerLevel = 0

  def setSpecies(self):
    self.animalSpecies = input('Enter species: ')

  def setAge(self):
    self.age = int(input('Enter age: '))

  def setThreatLevel(self):
    x = int(input('Enter threat level [1-10]: '))
    if x >= 8:
      self.threatLevel = 'aggressive'
    elif x >= 4:
      self.threatLevel = 'narky'
    else:
      self.threatLevel = 'peaceful'
    return self.threatLevel

  def setHungerLevel(self):
    self.hungerLevel = int(input('Enter hunger level: '))

cat = Animal()
cat.setSpecies()
cat.setAge()
print(cat.setThreatLevel())
cat.setHungerLevel()
