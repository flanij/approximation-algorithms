import time
from fits import *


with open('bin.txt', 'r') as inFile:
    # The first line is the number of test cases,
    test_cases = int(inFile.readline().rstrip())

    for _ in range(test_cases):
        # followed by the capacity of bins for tha test case
        capacity = int(inFile.readline().rstrip())

        #  the number of items 
        num_items = int(inFile.readline().rstrip())

        # then the weight of each item. 
        line = inFile.readline().rstrip('\n').split(' ')
        weights = [int(i) for i in line]


        # output to the terminal the number of bins each algorithm calculated for 
        # each test case. Your code should also collect and output the running 
        # time of each algorithm

        ## FF
        start_time = time.time()
        a = firstFit(capacity, num_items, weights)
        b = round((time.time() - start_time) * 1000000,2)

         ## BF
        start_time = time.time()
        e = bestFit(capacity, num_items, weights)
        f = round((time.time() - start_time) * 1000000,2)

        ## DFF
        start_time = time.time()
        c = firstFitDecreasing(capacity, num_items, weights)
        d = round((time.time() - start_time) * 1000000,2)


        string = "Test Case " + str(_+1) + " First Fit: " + str(a) + ", "+ str(b) +". "
        string += "First Fit Decreasing: "+ str(c)+", "+ str(d)+". "
        string += "Best Fit: "+ str(e)+ ", "+str(f)+"."

        print (string)