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
