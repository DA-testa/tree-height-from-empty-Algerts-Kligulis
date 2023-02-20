# python3

# import numpy as np
import sys
import threading


def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here



    return max_height


def main():
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    
    IorF = input() #.split('\\r\\n')
    if 'F' == IorF:
        # with open("./test/" + input(), mode="r") as fails:
        #     n = int(fails.readline())
        #     # arr = np.array(fails.readline().split())
        #     arr = fails.readline().split()
        #     max_height = 0
        #     for x in range(n):
        #         height = 1
        #         i = int(arr[x])
        #         while i != -1:
        #             i = int(arr[i])
        #             height += 1
        #         if max_height < height: max_height = height 
        #     print(max_height)
        print(1)

    elif 'I' == IorF:
        # n = int(input().replace('\r',''))
        # arr = input().split()
        # max_height = 0
        # for x in range(n):
        #     height = 1
        #     i = int(arr[x])
        #     while i != -1:
        #         i = int(arr[i])
        #         height += 1
        #     if max_height < height: max_height = height
        # print(max_height)
        print(2)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
