def create_graph(n):

  graph = {}
  for y in range(n):
    for x in range(n):
      graph[(x, y)] = []
      for i_y in range(-1, 2):
        for i_x in range(-1, 2):
          X = x + i_x
          Y = y + i_y
          if X not in [-1, n] and Y not in [-1, n] and (X, Y) != (x, y):
            graph[(x, y)].append((X, Y))
          
  return graph