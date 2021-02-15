from math import log
from random import randint

class YRobot:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.orientation = 0
    self.ultraSoundTopLeft = 0
    self.ultraSoundTopRight = 0
  
  def move_forward(self):
    try:
      ## Gestion X
      if (self.orientation == 0): self.x = self.x + 1
      # On gère +/-90 degrés à l'aide de la valeur absolue
      elif (self.orientation != 0 and abs(self.orientation) != 90):
        self.x = self.x + (1 * log(abs(self.orientation)))

      ## Gestion Y
      if (self.orientation > 0):
        self.y = self.y + (1 * log(abs(self.orientation)))
      if (self.orientation < 0):
          self.y = self.y - log(abs(self.orientation))
    except: pass
    print(self)
  
  def move_rearward(self):
    try:
      ## Gestion X
      if (self.orientation == 0): self.x = self.x - 1
      # On gère +/-90 degrés à l'aide de la valeur absolue
      elif (self.orientation != 0 and abs(self.orientation) != 90):
        self.x = self.x - (1 * log(abs(self.orientation)))

      ## Gestion Y
      if (self.orientation > 0):
        self.y = self.y + (1 * log(abs(self.orientation)))
      if (self.orientation < 0):
        self.y = self.y - log(abs(self.orientation))
    except: pass
    print(self)
  

  def turn_left(self):
    self.orientation = self.orientation - 30
    print(self)
  
  def turn_right(self):
    self.orientation = self.orientation + 30
    print(self)

  def __repr__(self):
    return '{ x:' + str(self.x) + \
          ', y:' + str(self.y) + \
          ', orientation: ' + str(self.orientation) + \
          ', ucTopLeft: ' + str(self.ultraSoundTopLeft) + \
          ', ucTopRight: ' + str(self.ultraSoundTopRight) + \
          ' }'

