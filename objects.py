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

  def place_merge_exit_(self):
    y = -1
    x  = random.randrange(self.grid_dim)
    self.exit = (x, y)
    self.graph[(self.exit)] = []
    for X in range (x - 1, x + 2):
      if (X, 0) in self.graph.keys():
        self.graph[(X, 0)].append(self.exit)
        self.graph[(self.exit)].append((X, 0))

  def place_player(self):
    y = self.grid_dim - 1
    x = random.randrange(self.grid_dim)
    self.player = (x, y)

  def place_enemy(self):
    y = 0
    x = random.randrange(self.grid_dim)
    self.enemy = (x ,y)

  def place_obstacle(self):
    objects = (self.grid_dim**2)//5
    counter = 0
    obstacles = []
    not_allowed_positions = [self.player, self.enemy, self.exit] + self.graph[(self.exit)]
    while counter < objects:
      obstacle = random.choice(list(self.graph))
      if obstacle not in not_allowed_positions:
        if a_star(self.graph, self.player, self.exit) != None:
          if a_star(self.graph, self.enemy, self.player) != None:
            counter += 1
            obstacles.append(obstacle)
            not_allowed_positions.append(obstacle)

    self.obstacles = obstacles
  
  def remove_obstacle_nodes(self):
    for node in self.obstacles:
      for neighbour in self.graph[node]:
        self.graph[neighbour].remove(node)

      self.graph[node] = []
  