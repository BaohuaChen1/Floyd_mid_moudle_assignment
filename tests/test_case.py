
# defining no path between two nodes
NO_PATH = 9999

# Test 1: testing a use case where there is only one node
test1 = [[0]]
output1 = [[0]]

# Test 2: Graph with 3 nodes 
test2 = [[0, NO_PATH, 9],
         [NO_PATH, 0, NO_PATH],
         [NO_PATH, 3, 0]]

output2 = [[0, 12, 9],
           [NO_PATH, 0, NO_PATH],
           [NO_PATH, 3, 0]]

# Test 3: Graph with 4 nodes 
test3 = [[0, 6, 2, NO_PATH],
         [NO_PATH, 0, NO_PATH, 2],
         [NO_PATH, NO_PATH, 0, 6],
         [NO_PATH, NO_PATH, NO_PATH, 0]]

output3 = [[0, 6, 2, 8],
           [NO_PATH, 0, NO_PATH, 2],
           [NO_PATH, NO_PATH, 0, 6],
           [NO_PATH, NO_PATH, NO_PATH, 0]]

# Test 4: Graph with 4 nodes 
test4 = [[0, 5, NO_PATH, 9],
         [4, 0, 8, NO_PATH],
         [NO_PATH, 3, 0, 5],
         [NO_PATH, 6, NO_PATH, 0]]

output4 = [[0, 5, 13, 9], 
           [4, 0, 8, 13], 
           [7, 3, 0, 5], 
           [10, 6, 14, 0]]



# Test 5: Graph with 6 nodes 
test5 = [[0, 7, NO_PATH, 5, NO_PATH, NO_PATH],
         [NO_PATH, 0, 2, NO_PATH, 9, NO_PATH],
         [3, NO_PATH, 0, NO_PATH, NO_PATH, NO_PATH],
         [2, NO_PATH, NO_PATH, 0, NO_PATH, 3],
         [NO_PATH, 3, 6, NO_PATH, 0, NO_PATH],
         [NO_PATH, NO_PATH, 2, NO_PATH, NO_PATH, 0]]

output5 = [[0, 7, 9, 5, 16, 8],
           [5, 0, 2, 10, 9, 13],
           [3, 10, 0, 8, 19, 11],
           [2, 9, 5, 0, 18, 3],
           [8, 3, 5, 13, 0, 16],
           [5, 12, 2, 10, 21, 0]]




