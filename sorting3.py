import matplotlib.pyplot as plt 
import math 
import random
import re
from timeit import default_timer as timer

# input sizes
input_sizes = [5,10,50,100,500,1000]

# definitions for our yvals and xvals 
yvals = []
xvals = [i for i in input_sizes]

# average_times will be stored for each input_size
average_times = []


def selectionSort(my_data):
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


# Our mergeSort function that takes in 'my_list' as the parrameter 
def mergeSort(my_data):                               # T(n)

    # function variables
    sorted_list = []                                    # 1

    # sorting stage

    # terminating case (n = 1)
    if len(my_data) == 1:
        return my_data                                    # 1 i.e. T(1) == O(1)

    # general case
    else:
        mid = int(len(my_data) / 2)                       # 1
        lefthalf = my_data[:mid]                          # 1
        righthalf = my_data[mid:]                         # 1

        lefthalf = mergeSort(lefthalf)                    # T(n/2)
        righthalf = mergeSort(righthalf)                  # T(n/2)

        # merge stage
        # occurs after both halves have been sorted
        # running time is O(n) as determined by           # O(n)
        # combined time of all while loops below

        i=0
        j=0

        # comparing lowest values while each list has contents
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                sorted_list.append(lefthalf[i])
                i=i+1
            else:
                sorted_list.append(righthalf[j])
                j=j+1

        # process remaining values from both lists
        while i < len(lefthalf):
            sorted_list.append(lefthalf[i])
            i=i+1

        while j < len(righthalf):
            sorted_list.append(righthalf[j])
            j=j+1

        return sorted_list

li = [selectionSort, mergeSort]

for func in li:

    # analysis stage of the code 
    # run trial on each input size
    for size in input_sizes:

        # record the times taken for each input size
        times = []
        # perform 20 trials
        for trial_number in range(20):
            # construct a random set of input data
            my_data = []
            for i in range(size):
                my_data.append(random.randint(-100,100))
            sorted_data = [] # blank list to hold sorted values

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




    func_name = re.search(r"<function (.*?) at (.*?)>", str(func)).group(1)

    plt.plot(xvals, average_times, label=str(func_name))

    average_times = []


yvals = []

"""
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
