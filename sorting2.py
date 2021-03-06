import matplotlib.pyplot as plt 
import math 
import random
from timeit import default_timer as timer

# input sizes
input_sizes = [ g for g in range(10000, 100000, 10000)]

# definitions for our yvals and xvals 
yvals = []
xvals = [i for i in input_sizes]

# average_times will be stored for each input_size
average_times = []

# Our mergeSort function that takes in 'my_list' as the parrameter 
def mergeSort(my_list):                               # T(n)

    # function variables
    sorted_list = []                                    # 1

    # sorting stage

    # terminating case (n = 1)
    if len(my_list) == 1:
        return my_list                                    # 1 i.e. T(1) == O(1)

    # general case
    else:
        mid = int(len(my_list) / 2)                       # 1
        lefthalf = my_list[:mid]                          # 1
        righthalf = my_list[mid:]                         # 1

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

# analysis stage of the code 
# run trial on each input size
for size in input_sizes:

    # record the times taken for each input size
    times = []
    # perform 20 trials
    for trial_number in range(3):
        # construct a random set of input data
        my_list = []
        for i in range(size):
            my_list.append(random.randint(-100,100))
        sorted_data = [] # blank list to hold sorted values

    
        # begin timer
        start = timer()
        print(f"Testing {mergeSort}, with input size {size}")
        mergeSort(my_list)    #   executes the analysis on the function 

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

#print(average_times, xvals)
yvals = []

plt.plot(xvals, average_times, label="Merge Sort")

yvals = []

plt.xlabel('Input Size')
plt.ylabel('Average Running Time')

plt.title("MergeSort Efficiency")

plt.legend()

plt.show()
