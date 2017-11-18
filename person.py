class Person:
  def __init__(self, name, age, gender, street, neighborhood):
    self.name = name
    self.age = age
    self.gender = gender
    self.street = street
    self.neighborhood = neighborhood

  def name(self):
    return self.name

  def gender(self):
    return self.gender

  def street(self):
    return self.street

  def neighborhood(self):
    return self.neighborhood
