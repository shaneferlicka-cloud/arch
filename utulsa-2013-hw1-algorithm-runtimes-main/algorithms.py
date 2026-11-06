# Shane Ferlicka
import time
import random

# for Polynomial time, we are implementing bubble sort
# bubble 
def bubbleSort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
    
        # Last i elements are already in place
        for j in range(0, n-i-1):
    
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == "__main__":

    # let's run the polynomial algorithm and gather data

    #create an array of integers and scramble them
    for index in range(1,101):
        arr = list(range(1,index * 1000))
        random.shuffle(arr)

    #start a timer
    start = time.time()

    #execute our function
    output = bubbleSort(arr)

    #stop our timer
    end = time.time()

    #print the results
    print(f"items: {index * 1000} runtime(s): {(end - start):.10f}")

