#3.* Common Elements Using Sets: Given two lists:
 
   # ```python
    #list1 = [1, 2, 3, 4, 5]
    #list2 = [3, 4, 5, 6, 7]
     #Find:
 #* Common elements.
 #* Elements present only in the first list.
 #* All unique elements from both lists.



list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

s1 = set(list1)
s2 = set(list2)

# Common elements
print("Common:", s1 & s2)

# Only first list
print("First list only:", s1 - s2)

# All unique elements
print("All unique:", s1 | s2)
