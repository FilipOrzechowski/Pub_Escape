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

