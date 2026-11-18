class Entity:
  def __init__(self, x:int, y:int):
    self.x = x
    self.y = y


class World:
  def __init__(self, high: int, wight:int):
    self.high = high
    self.wight = wight
    self.entities = list[Entity] = []

  def add_entity(self, entity: Entity):
    self.entities.append(entity)

class Renderer:
  def __init__(self):
    pass


class Engine:
  def __init__(self):
    pass
