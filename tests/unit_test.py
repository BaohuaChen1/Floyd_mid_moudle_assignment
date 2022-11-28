import unittest
import test_case
import floyd_recursive

class Test_floyd(unittest.TestCase):  #using the unittest 
    
    def test1(self):
        result = floyd_recursive.floyd(test_case.test1)   # importing the testing case
        shortest_graph = test_case.output1
        self.assertEqual(result, shortest_graph, "Output incorrect")   #to test whether the testing output equals to the expected output
                
    def test2(self):
        result = floyd_recursive.floyd(test_case.test2)
        shortest_graph = test_case.output2
        self.assertEqual(result, shortest_graph, "Output incorrect")

               
    def test3(self):
        result = floyd_recursive.floyd(test_case.test3)
        shortest_graph = test_case.output3
        self.assertEqual(result, shortest_graph, "Output incorrect")
     
               
    def test4(self):
    
        result = floyd_recursive.floyd(test_case.test4)
        shortest_graph = test_case.output4
        self.assertEqual(result, shortest_graph, "Output incorrect")
                
    def test5(self):
        result = floyd_recursive.floyd(test_case.test5)
        shortest_graph = test_case.output5
        self.assertEqual(result, shortest_graph, "Output incorrect")

if __name__ == '__main__':
    unittest.main()
