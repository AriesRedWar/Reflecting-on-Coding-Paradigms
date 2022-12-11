def new_line():
    print("---------Original------------")
# new_line()

def new_line_repair():
    print("---------repair------------")
# new_line_repair()

def new_line_speed():
    print("---------Speed------------")
# new_line_speed()

def new_line_flame():
    print("---------Flame------------")
# new_line_flame()


# Watto needs a new system for organizing his inventory of podracers. 
# Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. 
class Podracer:
  def __init__(self, name, max_speed, condition, price):
    self.name = name
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  # Define a repair() method that will update the condition of the podracer to "repaired".
  def repair(self):
    self.condition = "repaired"
    
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, name, max_speed, condition, price):
    super().__init__(name, max_speed, condition, price)
  
  def boost(self):
    self.max_speed *= 2
    
# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
  def __init__(self, name, max_speed, condition, price):
    super().__init__(name, max_speed, condition, price)
  
  def flame_jet(self,other):
    other.condition = "trashed"

# Make sure to answer the following prompts about your coding experience:
# Q-1 How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
# A-1 Inheritance using the super class, Polymorphism is used with us defining methods in the child classes that have the same name as the parents
 
# Q-2 Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
# A-2 at this time im not sure if it would have been easier in a diffrent coding style still learning the diffrences and what would be the best solution on how to implement them.

# Q-3 How in particular did Object Oriented Programming assist in the solving of this problem?
# A-3 it allowed me to be able to change the conditions and access the data to be updated to new settings.


pod1 = Podracer(name="pod1", max_speed=2, condition='fast', price=200)
pod2 = AnakinsPod(name="pod2", max_speed=4, condition='fast', price=200)
pod3 = SebulbasPod(name="pod3", max_speed=5, condition='fast', price=200)

import pprint
new_line()
pprint.pprint(vars(pod1))
new_line_repair()
pod1.repair()
pprint.pprint(vars(pod1))

new_line()
pprint.pprint(vars(pod2))
new_line_speed()
pod2.boost()
pprint.pprint(vars(pod2))

new_line()
pprint.pprint(vars(pod3))
new_line_flame()
pod3.flame_jet(pod3)
pprint.pprint(vars(pod3))
