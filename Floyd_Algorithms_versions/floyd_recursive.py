import itertools

"""This is recursive version of Floyd's algorithm which is modified by the given example."""

def floyd(distance):
    
    MAX_LENGTH = len(distance) # Define the number of nodes in the given graph
 
    
    def recursive(start_node, end_node, intermediate):
        if intermediate < 0:   # Calculates the direct paths and exits the recursion, only when all intermediate nodes have been tried
            return distance[start_node][end_node]

        else:   #If there is a new shorter route through the intermediate, return the minimum between two paths with a different intermediate end
                # node, shortest path between the start point and the intermediate point,plus the intermediate point and the end point
            
          direct_path = recursive(start_node, end_node, intermediate - 1)
          intermediate_path_1 = recursive(start_node, intermediate, intermediate - 1)
          intermediate_path_2 = recursive(intermediate, end_node, intermediate - 1)
          return min(direct_path, intermediate_path_1 + intermediate_path_2)  

    for intermediate, start_node, end_node    in itertools.product    (range(MAX_LENGTH),repeat=3):
        #return all possible paths and find the minimum
        distance[start_node][end_node] = recursive(start_node,end_node,intermediate)
    return distance

