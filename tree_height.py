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
    
    IorF = input().replace('\r','') #.split('\\r\\n')
    if 'F' == IorF:
        # with open(input().replace('\r','') + '.txt', mode="r") as fails:
        with open("./test/" + input().replace('\r',''), mode="r") as fails:
            n = int(fails.readline())
            # arr = np.array(fails.readline().split())
            arr = fails.readline().split()
            max_height = 0
            
            heightList = [0] * n
            
            for x in range(n):
                height = 1
                i = int(arr[x])
                # if heightList[i]!=0:
                #     heightList[x] = heightList[i]+1
                #     if max_height < heightList[x]: max_height = heightList[x]
                #     continue
                if i != -1 and heightList[i]!=0:
                    heightList[x] = heightList[i]+1
                    if max_height < heightList[x]: max_height = heightList[x]
                    continue
                while i != -1:
                    i = int(arr[i])
                    if i != -1 and heightList[i]!=0:
                        height = height + heightList[i]
                        break
                    height += 1
                if max_height < height: max_height = height
                heightList[x] = height
                
                i = int(arr[x])
                while i != -1:
                    if i != -1 and heightList[i]!=0:
                        break
                    height -= 1
                    heightList[i] = height
                    i = int(arr[i])
            print(max_height)

    elif 'I' in IorF:
        n = int(input().replace('\r',''))
        arr = input().split()
        max_height = 0
        
        heightList = [0] * n
        
        for x in range(n):
            height = 1
            i = int(arr[x])
            # if heightList[i]!=0:
            #     heightList[x] = heightList[i]+1
            #     if max_height < heightList[x]: max_height = heightList[x]
            #     continue
            if i != -1 and heightList[i]!=0:
                heightList[x] = heightList[i]+1
                if max_height < heightList[x]: max_height = heightList[x]
                continue
            while i != -1:
                i = int(arr[i])
                if i != -1 and heightList[i]!=0:
                    height = height + heightList[i]
                    break
                height += 1
            if max_height < height: max_height = height
            heightList[x] = height
            
            i = int(arr[x])
            while i != -1:
                if i != -1 and heightList[i]!=0:
                    break
                height -= 1
                heightList[i] = height
                i = int(arr[i])
        print(max_height)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
