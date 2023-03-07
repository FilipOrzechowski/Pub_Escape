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
  def choose_direction(self, choice):
    if choice == "w":
      next_node = (self.player[0], self.player[1] - 1)

    elif choice == "e":
      next_node = (self.player[0] + 1, self.player[1] - 1)
    
    elif choice == "d":
      next_node = (self.player[0] + 1, self.player[1])
    
    elif choice == "c":
      next_node = (self.player[0] + 1, self.player[1] + 1)
    
    elif choice == "x":
      next_node = (self.player[0], self.player[1] + 1)
    
    elif choice == "z":
      next_node = (self.player[0] - 1, self.player[1] + 1)
    
    elif choice == "a":
      next_node = (self.player[0] - 1, self.player[1])
    
    elif choice == "q":
      next_node = (self.player[0] - 1, self.player[1] - 1)
    
    elif choice == "s":
      next_node = self.player
    
    return next_node
  
  def change_player_position(self):
    choice = input("Choose a direction!")
    next_node = self.choose_direction(choice)
    possible_nodes = self.graph[self.player] + [self.player]
    while choice not in ["w", "e", "d", "c", "x", "z", "a", "q", "s"] or next_node not in possible_nodes:
      choice = input("Wrong button! Choose a direction!")

    self.player = self.choose_direction(choice)

  def change_enemy_position(self):
    input("Press enter to let your enemy change position")
    next_node = a_star(self.graph, self.enemy, self.player)[1]
    self.enemy = next_node

  def print_map(self):
    game_map = ""
    for y in range(-1, self.grid_dim):
      for x in range(self.grid_dim):
        if (x, y) in self.obstacles:
          game_map += "|  X  "
        
        elif (x, y) == self.player and (x, y) not in [self.enemy, self.exit]:
          game_map += "|  *  "

        elif (x, y) == self.enemy:
          game_map += "|  @  "
        
        elif y == -1:
          if x == self.exit[0]:
            game_map += "|EXIT |"

          else:
            game_map += "      "
        
        else:
          game_map += "|     "

      if y != -1:
        game_map += "|\n" 

      else:
        game_map += "\n"

      game_map += "------"*self.grid_dim + "-\n"

    print(game_map)
  
  def create_complete_map(self):
    self.place_merge_exit_()
    self.place_player()
    self.place_enemy()
    self.place_obstacle()
    self.remove_obstacle_nodes()
    self.print_map()  