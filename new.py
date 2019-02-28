# timed selection sort implementation
import matplotlib.pyplot as plt 
import math 
import random
from timeit import default_timer as timer

# input sizes
input_sizes = [5,10,20,50,100,500,1000]


yvals = []
xvals = [i for i in input_sizes]


# average_times will be stored for each input_size
average_times_1 = []
average_times_2 = []

# run trial on each input size
for size in input_sizes:

 # record the times taken for each input size
 times_1 = []
 times_2 = []

 # perform 20 trials
 for trial_number in range(20):

   # construct a random set of input data
   my_data = []
   for i in range(size):
     my_data.append(random.randint(-100,100))
   sorted_data = [] # blank list to hold sorted values

   # print("input:", my_data)   # uncomment this line to output the original list

   # begin timer
   start = timer()

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
yvals = []

# for n in average_times:
#     yvals.append(n)


plt.plot(xvals, average_times, label="Destructive Selection Sort")

yvals = []



plt.xlabel('Input Size')
plt.ylabel('Average Running Time')

plt.title("Sorting Algorithm performance ")

plt.legend()

plt.show()