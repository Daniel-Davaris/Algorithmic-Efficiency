# selection sort implementation
my_data = [5,9,2,14,-5,7,8,9,1,37]
sorted_data = [] # blank list to hold sorted values

print("input:", my_data) 

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

# sorted_data is now the sorted version of the original list
print("result", sorted_data)
