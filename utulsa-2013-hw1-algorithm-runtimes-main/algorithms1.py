# Shane Ferlicka
import time
import random
import matplotlib.pyplot as plt

# for Polynomial time, we are implementing bubble sort bubble 
def bubbleSort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
    
        # Last i elements are already in place
        for j in range(0, n-i-1):
    
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == "__main__":

    for index in range(1,11):
        arr = list(range(1,index * 100))
        random.shuffle(arr)

    #start a timer
    start = time.time()

    #execute our function
    output = bubbleSort(arr)

    #stop our timer
    end = time.time()

    #print the results
    print(f"items: {index * 100} runtime(s): {(end - start):.10f}")

# ============================================================
# HOMEWORK 1 - ALGORITHM RUNTIME ANALYSIS
#
# The code below tests seven different runtime classes:
# constant, logarithmic, linear, quadratic, cubic, exponential, and factorial.
#
# Each algorithm is tested with increasing input sizes.
# It records how long each test takes and then use Matplotlib to graph the results run times of each.
# ============================================================


# ------------------------------------------------------------
# CONSTANT TIME - O(1)
# ------------------------------------------------------------

def constantTime(arr):
    # Constant time only performs one operation, no matter how large the input becomes.
    return arr[0]


# Lists that will hold our graph data.
constant_sizes = []
constant_times = []

# Test at least 10 different input sizes.
for size in range(1000, 11000, 1000):

    # Create an input list.
    arr = list(range(size))

    # Start the timer.
    start = time.time()

    # Run the constant time algorithm.
    constantTime(arr)

    # Stop the timer.
    end = time.time()

    # Save the input size and runtime.
    constant_sizes.append(size)
    constant_times.append(end - start)
    print(f"Constant input: {size}, Runtime: {(end - start):.10f} seconds")


# Plot the constant time results.
plt.figure()
plt.plot(constant_sizes, constant_times, marker='o')
plt.title("Constant Runtime - O(1)")
plt.xlabel("Input Size")
plt.ylabel("Runtime (seconds)")
plt.grid()
plt.show()


# ------------------------------------------------------------
# LOGARITHMIC TIME - O(log n)
#
# Binary search is a logarithmic algorithm because each loop removes half of the remaining search area.
# ------------------------------------------------------------

def binarySearch(arr, target):

    # Start at the beginning and end of the list.
    low = 0
    high = len(arr) - 1

    while low <= high:

        # Find the middle of the remaining list.
        middle = (low + high) // 2

        # We found the target.
        if arr[middle] == target:
            return middle

        # Target must be in the right half.
        elif arr[middle] < target:
            low = middle + 1

        # Target must be in the left half.
        else:
            high = middle - 1

    # Target was not found.
    return -1


log_sizes = []
log_times = []

for size in range(10000, 110000, 10000):

    # Binary search requires a sorted list.
    arr = list(range(size))

    start = time.time()

    # Search for -1 so the algorithm must continue until it determines the item is not present.
    binarySearch(arr, -1)

    end = time.time()

    log_sizes.append(size)
    log_times.append(end - start)
    print(f"Logarithmic input: {size}, Runtime: {(end - start):.10f} seconds")


plt.figure()
plt.plot(log_sizes, log_times, marker='o')
plt.title("Logarithmic Runtime - O(log n)")
plt.xlabel("Input Size")
plt.ylabel("Runtime (seconds)")
plt.grid()
plt.show()


# ------------------------------------------------------------
# LINEAR TIME - O(n)
#
# A linear algorithm looks at every item once.
# ------------------------------------------------------------

def linearTime(arr):

    total = 0

    # Visit every item in the list one time.
    for number in arr:
        total += number

    return total


linear_sizes = []
linear_times = []

for size in range(10000, 110000, 10000):

    arr = list(range(size))

    start = time.time()

    linearTime(arr)

    end = time.time()

    linear_sizes.append(size)
    linear_times.append(end - start)
    print(f"Linear input: {size}, Runtime: {(end - start):.10f} seconds")


plt.figure()
plt.plot(linear_sizes, linear_times, marker='o')
plt.title("Linear Runtime - O(n)")
plt.xlabel("Input Size")
plt.ylabel("Runtime (seconds)")
plt.grid()
plt.show()


# ------------------------------------------------------------
# QUADRATIC TIME - O(n^2)
#
# We already have bubbleSort() above, so I reuse the existing function instead of making another one.
# Bubble sort uses nested loops, giving it quadratic runtime.
# ------------------------------------------------------------

quadratic_sizes = []
quadratic_times = []

for size in range(100, 1100, 100):

    # Create a list.
    arr = list(range(size))

    # Shuffle it because bubble sort needs unsorted data.
    random.shuffle(arr)

    start = time.time()

    # Use the bubbleSort function that was already provided.
    bubbleSort(arr)

    end = time.time()

    quadratic_sizes.append(size)
    quadratic_times.append(end - start)
    print(f"Quadratic input: {size}, Runtime: {(end - start):.10f} seconds")


plt.figure()
plt.plot(quadratic_sizes, quadratic_times, marker='o')
plt.title("Bubble Sort - Quadratic Runtime O(n^2)")
plt.xlabel("Input Size")
plt.ylabel("Runtime (seconds)")
plt.grid()
plt.show()


# ------------------------------------------------------------
# CUBIC TIME - O(n^3)
#
# Three nested loops represent cubic runtime.
# ------------------------------------------------------------

def cubicTime(n):

    count = 0

    # First loop runs n times.
    for i in range(n):

        # Second loop also runs n times.
        for j in range(n):

            # Third loop also runs n times.
            for k in range(n):

                # Perform a simple operation.
                count += 1

    return count


cubic_sizes = []
cubic_times = []

# Cubic runtime gets slow quickly, so we use smaller input sizes.
for size in range(10, 110, 10):

    start = time.time()

    cubicTime(size)

    end = time.time()

    cubic_sizes.append(size)
    cubic_times.append(end - start)
    print(f"Cubic input: {size}, Runtime: {(end - start):.10f} seconds")


plt.figure()
plt.plot(cubic_sizes, cubic_times, marker='o')
plt.title("Cubic Runtime - O(n^3)")
plt.xlabel("Input Size")
plt.ylabel("Runtime (seconds)")
plt.grid()
plt.show()


# ------------------------------------------------------------
# EXPONENTIAL TIME - O(2^n)
#
# This function generates every possible subset.
# For n items there are 2^n possible subsets.
# ------------------------------------------------------------

def exponentialTime(n):

    count = 0

    # 2 ** n means 2 raised to the power of n.
    # This loop therefore runs 2^n times.
    for i in range(2 ** n):
        count += 1

    return count


exponential_sizes = []
exponential_times = []

# Exponential algorithms become slow extremely quickly, so the input sizes must stay relatively small.
for size in range(10, 20):

    start = time.time()

    exponentialTime(size)

    end = time.time()

    exponential_sizes.append(size)
    exponential_times.append(end - start)
    print(f"Exponential input: {size}, Runtime: {(end - start):.10f} seconds")


plt.figure()
plt.plot(exponential_sizes, exponential_times, marker='o')
plt.title("Exponential Runtime - O(2^n)")
plt.xlabel("Input Size")
plt.ylabel("Runtime (seconds)")
plt.grid()
plt.show()


# ------------------------------------------------------------
# FACTORIAL TIME - O(n!)
#
# This function generates every possible ordering (permutation) of n items.
# ------------------------------------------------------------

def factorialTime(items):

    # If there are zero or one items left, there is only one possible ordering.
    if len(items) <= 1:
        return 1

    count = 0

    # Try each item in the first position.
    for i in range(len(items)):

        # Make a new list without the current item.
        remaining = items[:i] + items[i + 1:]

        # Count every possible ordering of the remaining items.
        # We count the permutations instead of storing them all, which uses much less memory and doesnt slow my computer down.
        count += factorialTime(remaining)

    return count


factorial_sizes = []
factorial_times = []

# Factorial runtime grows extremely fast.
# 1 through 10 gives us 10 data points, but the last few tests can take noticeably longer.
for size in range(1, 11):

    # Create a list containing "size" items.
    arr = list(range(size))

    start = time.time()

    factorialTime(arr)

    end = time.time()

    factorial_sizes.append(size)
    factorial_times.append(end - start)
    print(f"Factorial input: {size}, Runtime: {(end - start):.10f} seconds")


plt.figure()
plt.plot(factorial_sizes, factorial_times, marker='o')
plt.title("Factorial Runtime - O(n!)")
plt.xlabel("Input Size")
plt.ylabel("Runtime (seconds)")
plt.grid()
plt.show()

