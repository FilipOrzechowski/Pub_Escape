import random
from algorithm import a_star

class Map_Objects():
  def __init__(self, func_create_graph, grid_dim):
    self.graph = func_create_graph(grid_dim)
    self.grid_dim = grid_dim
    self.exit= None
    self.enemy = None
    self.player = None
    self.obstacles = None