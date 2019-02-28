import matplotlib.pyplot as plt 
import math 
import random
import re
from timeit import default_timer as timer

# input sizes
input_sizes = [x for x in range(1000, 100000, 10000)]

# definitions for our yvals and xvals 
yvals = []
xvals = [i for i in input_sizes]

# average_times will be stored for each input_size
average_times = []

def split_list(my_data):
    half = len(my_data) // 2 # 2
    return [my_data[:half], my_data[half:]] # 4

sorted_data = []

def selection_Sort(my_data):
    # perform sort
    # find lowest value in list - continue while we still have values
    while len(my_data) > 0:
        
        # each time through reset the lowest value
        lowest = None

        # step through list, looking for lowest value
        for item in my_data:
            if lowest == None or lowest > item:
                lowest = item

        # append the lowest value to the sorted list
        sorted_data.append(lowest)

        # remove the value from the original list
        my_data.remove(lowest)

        return sorted_data


def mergeSort(my_data):
    # Exit condition
    if len(my_data) == 1: # 1
        return my_data # 1

    # halve array
    a, b = split_list(my_data) # 6
    # sort halves
    a = mergeSort(a)[::-1] # log(n) + 1
    b = mergeSort(b)[::-1] # log(n) + 1

    # empty array
    my_data = [] # 1
    while a or b: # while comparisons # n
        # Empty B list
        if a and not b: # 1
            my_data.extend(a[::-1]) # 1
            break
        # Empty A list
        elif b and not a: # 1
            my_data.extend(b[::-1]) # 1
            break
        # A less then B
        elif a[-1] <= b[-1]: # 1
            my_data.append(a.pop()) # 1
        # B less then A
        else: # 1
            my_data.append(b.pop()) # 1
    """Merge sort effeciency: (1 + 1 + 6 + 2 + 2log(n))^(n+1+1+1+1+1+1) = 10 + 2log(n^n+6) = 10 + 2(n+6)log(n)"""
    return my_data # 1

li = [mergeSort,selection_Sort]

for func in li:
    func_name = re.search(r"<function (.*?) at (.*?)>", str(func)).group(1)
    # analysis stage of the code 
    # run trial on each input size
    for size in input_sizes:

        # record the times taken for each input size
        times = []
        # perform 20 trials
        for trial_number in range(3):
            # construct a random set of input data
            my_data = []
            for i in range(size):
                my_data.append(random.randint(-100,100))
            print(f"Testing {func_name}, with input size {len(my_data)}")
            # begin timer for selection sort 
            start = timer()
            func(my_data)    #   executes the analysis on the function 

            # end timer
            end = timer()

            # calculate running time (measured in seconds)
            running_time = end - start
            # add it to our list of times
            times.append(running_time)
            # print(running_time)

        # sorted_data is now the sorted version of the original list
        # print("result", sorted_data)  # uncomment this line to see the sorted version
        # calculate the average time and append to our list of average_times
        average_times.append(sum(times) / float(len(times)))  # float just in case python 2 is used

    # print average "running times" for each input size
    for i in range(len(input_sizes)):
        print("Running time for input size",input_sizes[i], "is", average_times[i])
    print(average_times, xvals)





    plt.plot(xvals, average_times, label=str(func_name))

    average_times = []

"""
yvals = []

for n in xvals:
    yvals.append(n**2)
plt.plot(xvals, yvals, label="y = x^2")

yvals = []
"""
plt.xlabel('Input Size')
plt.ylabel('Average Running Time')

plt.title("Selection Sort VS MergeSort Efficiency")

plt.legend()

plt.show()
