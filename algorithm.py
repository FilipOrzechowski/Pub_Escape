def get_min_distance(distance_and_node_list):
  min_distance = float('inf')
  index = None
  for i in range(len(distance_and_node_list)):
    if distance_and_node_list[i][0] < min_distance:
      min_distance = distance_and_node_list[i][0]
      node = distance_and_node_list[i][1]
      index = i
      
  distance_and_node_list.remove(distance_and_node_list[index])
  return min_distance, node


def heuristic(start, target):
  x_distance = abs(start[0] - target[0])
  y_distance = abs(start[1] - target[1])
  return (x_distance**2 + y_distance**2)**.5


def a_star(graph, start, target):
  paths_and_distances = {}
  for node in graph:
    paths_and_distances[node] = [float('inf'), [start]]

  paths_and_distances[start][0] = 0
  nodes_to_explore = [(0, start)]
  while nodes_to_explore and paths_and_distances[target][0] == float('inf'):
    current_distance, current_node = get_min_distance(nodes_to_explore)

    for neighbor in graph[current_node]:
      new_distance = current_distance + 1 + heuristic(neighbor, target)
      temp = paths_and_distances[current_node][1]
      new_path = temp+[neighbor]
      if new_distance < paths_and_distances[neighbor][0]:
        paths_and_distances[neighbor][0] = new_distance
        paths_and_distances[neighbor][1] = new_path
        nodes_to_explore.append((new_distance, neighbor))
        
  if paths_and_distances[target][0] != float('inf'):
    return paths_and_distances[target][1]
  
  else:
    return None