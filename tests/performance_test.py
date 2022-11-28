import test_case
import floyd_recursive
import floyd_imperative
import time

#Performance testing for the recurstive version
test = [test_case.test1, test_case.test2, test_case.test3, test_case.test4, test_case.test5]
number = 1
for i in test: 
    start_time = time.perf_counter()
    floyd_recursive.floyd(i)   # running the testing case
    print(f"Time for the recursive test in case {number} is : {time.perf_counter()-start_time:.8f}s")
    number += 1

#Performance testing of for the imperative version
test = [test_case.test1, test_case.test2, test_case.test3, test_case.test4, test_case.test5]
number = 1
for j in test:
    start_time = time.perf_counter()
    floyd_imperative.floyd(j)
    print(f"Time for the imperative test in case{number} is : {time.perf_counter()-start_time:.8f}s")
    number += 1
    


