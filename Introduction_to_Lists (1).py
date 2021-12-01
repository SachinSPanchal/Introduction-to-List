#!/usr/bin/env python
# coding: utf-8

# ### Earlier when discussing strings we introduced the concept of a <u>sequence</u> in Python. 
# * <u>Lists</u> can be thought of the most general version of a *sequence* in Python. 
# 
# 
# * Unlike strings, they are mutable, meaning the elements inside a list can be changed! 
# 
# 
# * Lists are constructed with brackets <code>[]</code> and commas separating every element in the list.

# In[ ]:


# Assign a list to an variable named my_list
my_list = [1,2,3,4]


# In[ ]:


print(my_list)


# In[ ]:


type(my_list)


# * We just created a list of integers, but lists can actually hold different object types. For example:

# In[ ]:


my_list = ['A string',23,100.232,'o',True]


# In[ ]:


my_list


# * Just like strings, the <code>len()</code> function will tell you how many items are in the sequence of the list.

# In[ ]:


len(my_list)


# ## List Indexing
# * Indexing work just like in strings.
# 
# 
# * A list index refers to the location of an element in a list.
# 
# 
# * Remember the indexing begins from 0 in Python. 
# 
# 
# * The first element is assigned an index 0, the second element is assigned an index of 1 and so on and so forth.

# In[ ]:


# Consider a list of strings
loss_functions = ['Mean Absolute Error','Mean Squared Error','Huber Loss','Log Loss','Hinge Loss']
print(loss_functions)


# In[ ]:


# Grab the element at index 0, which is the FIRST element
print(loss_functions[0])


# In[ ]:


len(loss_functions)


# In[ ]:


# Grab the element at index 3, which is the FOURTH element
print(loss_functions[3])


# In[ ]:


print(loss_functions[6])


# In[ ]:


# Grab the element at the index -1, which is the LAST element
print(loss_functions[-1])


# In[ ]:


# Grab the element at the index -3, which is the THIRD LAST element
print(loss_functions[-3])


# ## List Slicing
# 
# * We can use a <code>:</code> to perform *slicing* which grabs everything up to a designated point. 
# 
# 
# * The starting index is specified on the left of the <code>:</code> and the ending index is specified on the right of the <code>:</code>. 
# 
# 
# * Remember the element located at the right index is not included.

# In[ ]:


# Print our list
print(loss_functions)


# In[ ]:


# Grab the elements starting from index 1 and everything past it
loss_functions[1:4]


# * If you do not specify the ending index, then all elements are extracted which comes after the starting index including the element at that starting index. The operation knows only to stop when it has run through the entire list.

# In[ ]:


# Grab everything starting from index 2
loss_functions[2:]


# * If you do not specify the starting index, then all elements are extracted which comes befores the ending index excluding the element at the specified ending index. The operation knows only to stop when it has extracted all elements before the  element at the ending index.

# In[ ]:


# Grab everything before the index 4
loss_functions[:4]


# * If you do not specify the starting and the ending index, it will extract all elements of the list.

# In[ ]:


# Grab everything
print(loss_functions[:])


# * We can also extract the last four elements. Remember we can use the index -4 to extract the FOURTH LAST element

# In[ ]:


# Grab the LAST FOUR elements of the list
loss_functions[-4:]


# In[ ]:


loss_functions[-10]


# * It should also be noted that list indexing will return an error if there is no element at that index.

# In[ ]:


len(loss_functions)


# In[ ]:


loss_functions[8]


# ## List Operations
# * Remember we said that lists are mutable as opposed to strings. Lets see how can we change the elements of a list

# * We can also use <code>+</code> to concatenate lists, just like we did for strings.

# In[ ]:


print(loss_functions)


# In[ ]:


loss_functions + ['Kullback-Leibler']


# * Note: This doesn't actually change the original list!

# In[ ]:


print(loss_functions)


# * You would have to reassign the list to make the change permanent.

# In[ ]:


# Reassign
loss_functions = loss_functions + ['Kullback-Leibler']


# In[ ]:


loss_functions


# * We can also use the <code>*</code> for a duplication method similar to strings:

# In[ ]:


# Make the list double
len(loss_functions * 6)


# ## List Functions

# ### <code>len()</code>
# 
# 
# * <code>len()</code> function returns the length of the list

# In[ ]:


print(loss_functions)


# In[ ]:


len(loss_functions)


# ### <code>min()</code>
# 
# 
# * <code>min()</code> function returns the minimum element of the list
# 
# 
# * <code>min()</code> function only works with lists of similar data types

# In[ ]:


new_list = [6, 9, 1, 3, 5.5]


# In[ ]:


min(new_list)


# In[ ]:


my_new_list = ['a','b', 'z' ,'y' , 'm']


# In[ ]:


min(my_new_list)


# ### <code>max()</code>
# 
# 
# * <code>max()</code> function returns the maximum element of the list
# 
# 
# * <code>max()</code> function only works with lists of similar data types

# In[ ]:


new_list = ['Argue','Burglar','Parent','Linear','shape']


# In[ ]:


max(new_list)


# ### <code>sum()</code>
# 
# 
# * <code>sum()</code> function returns the sum of the elements of the list
# 
# 
# * <code>sum()</code> function only works with lists of numeric data types

# In[ ]:


new_list = [6, 9, 1, 3, 5.5]


# In[ ]:


sum(new_list)


# ### <code>sorted()</code>
# 
# 
# * <code>sorted()</code> function returns the sorted list 
# 
# 
# * <code>sorted()</code> function takes reverse boolean as an argument
# 
# 
# * <code>sorted()</code> function only works on a list with similar data types

# In[ ]:


new_list


# In[ ]:


sorted(new_list)


# In[ ]:


print(new_list)


# In[ ]:


new_list = ['Argue','Burglar','Parent','Linear','shape']


# In[ ]:


sorted(new_list)


# In[ ]:


print(new_list)


# In[ ]:


sorted(new_list,reverse=True)


# In[ ]:


sorted(new_list)


# * <code>sorted()</code> function does not change our list

# In[ ]:


new_list


# ## List Methods
# 
# * If you are familiar with another programming language, you might start to draw parallels between arrays in another language and lists in Python. Lists in Python however, tend to be more flexible than arrays in other languages for a two good reasons: they have no fixed size (meaning we don't have to specify how big a list will be), and they have no fixed type constraint (like we've seen above).
# 
# 
# * Let's go ahead and explore some more special methods for lists:

# In[ ]:


# Create a new list
my_list = [1,2,3,1,1,1,3,10,5,8]


# ### <code>append()</code> 
# 
# * Use the <code>append()</code> method to permanently add an item to the end of a list.
# 
# 
# * <code>append()</code> method takes the element which you want to add to the list as an argument

# In[ ]:


# Print the list
my_list


# In[ ]:


len(my_list)


# In[ ]:


# Append to the end of the list
my_list.append('Append me!')


# * Ah darn it! I was expecting some output. Lets see what happened to <code>my_list</code>

# In[ ]:


print(my_list)


# In[ ]:


len(my_list)


# * Woah! Calling the <code>append()</code> method changed my list? Yes, the <code>append()</code>  method changes your original list!

# In[ ]:


# Show
my_list.append(2.73)


# In[ ]:


print(my_list)


# * We can in fact add a list object to our <code>my_list</code> object

# In[ ]:


my_list.append([1,2,3])


# In[ ]:


my_list


# In[ ]:


len(my_list)


# In[ ]:


my_list.append([10,[19,20],30])


# In[ ]:


len(my_list)


# ### <code>extend()</code>
# 
# * Use the <code> extend()</code> method to merge a list to an existing list
# 
# 
# * <code> extend()</code> method takes a list or any iterable(don't worry about it now) as an argument.
# 
# 
# * Quite helpful when you have two or more lists and you want to merge them together

# In[ ]:


# Print the list
print(my_list)


# In[ ]:


my_list.extend(['Wubba','Lubba','Dub Dub'])


# In[ ]:


print(my_list)


# In[ ]:


len(my_list)


# ### <code>pop()</code>
# 
# * Use <code>pop()</code> to "pop off" an item from the list. 
# 
# 
# * By default <code>pop()</code> takes off the element at the last index, but you can also specify which index to pop off. 
# 
# 
# * <code>pop()</code> takes the index as an argument and returns the elenent which was popped off.

# In[ ]:


# Print the list
print(my_list)


# In[ ]:


# Pop off the 0 indexed item
my_list.pop()


# * <code>pop()</code> method changes the list by popping off the element at the specified index

# In[ ]:


print(my_list)


# In[ ]:


# Assign the popped element, remember default popped index is -1
my_list.pop(-1)


# In[ ]:


len(my_list)


# In[ ]:


print(my_list)


# ### <code>remove()</code>
# 
# * Use <code>remove()</code> to remove an item/element from the list. 
# 
# 
# * By default <code>remove()</code> removes the specified element from the list.
# 
# 
# * <code>remove()</code> takes the element as an argument.

# In[ ]:


# Print the list
print(my_list)


# In[ ]:


# Remove the element which you want to 
my_list.remove([10, [19, 20], 30])


# In[ ]:


# Show
print(my_list)


# In[ ]:


my_list.remove([1,2,3])


# In[ ]:


print(my_list)


# In[ ]:


len(my_list)


# In[ ]:


my_list.remove(1)


# In[ ]:


print(my_list)


# In[ ]:


len(my_list)


# In[ ]:


my_list.clear


# ### <code>count()</code>
# 
# 
# * The <code>count()</code> method returns the total occurrence of a specified element in the list

# In[ ]:


print(my_list)


# In[ ]:


# Count the number of times element 1 occurs in my_list
my_list.count('Wubba')


# In[ ]:


my_list.count(1)


# ### <code>index()</code>
# 
# 
# * The <code>index()</code> method returns the index of a specified element.

# In[ ]:


print(my_list)


# In[ ]:


my_list.index('Wubba')


# In[ ]:


my_list.index(3)


# ### <code>sort()</code>
# 
# * Use <code>sort()</code> to sort the list in either ascending/descending order
# 
# 
# * The sorting is done in ascending order by default
# 
# 
# * <code>sort()</code> method takes the reverse boolean as an argument
# 
# 
# * <code>sort()</code> method only works on a list with elements of same data type

# In[ ]:


new_list = [6, 9, 1, 3, 5]


# In[ ]:


# Use sort to sort the list (this is permanent!)
new_list.sort()


# In[ ]:


print(new_list)


# In[ ]:


# Use the reverse boolean to set the ascending or descending order
new_list.sort(reverse=True)
print(new_list)


# In[ ]:


boolean_list = [True, False]


# In[ ]:


boolean_list.sort(reverse=True)


# In[ ]:


print(boolean_list)


# ### <code>reverse()</code>
# 
# * <code>reverse()</code> method reverses the list

# In[ ]:


my_list = [1, 1, 1, 1, 1.43, 2, 3, 3, 5, 8, 10, 'Lubba', 'Dub Dub']


# In[ ]:


print(my_list)


# In[ ]:


my_list.reverse()


# In[ ]:


print(my_list)


# ## Nested Lists
# 
# * A great feature of of Python data structures is that they support *nesting*. This means we can have data structures within data structures. For example: A list inside a list.

# In[ ]:


# Let's make three lists
lst_1=[1,2,3]
lst_2=['b','a','d']
lst_3=[7,8,9]

# Make a list of lists to form a matrix
list_of_lists = [lst_1,lst_2,lst_3]


# In[ ]:


print(list_of_lists)


# In[ ]:


# Show
type(list_of_lists)


# In[ ]:


# Grab first item in matrix object
list_of_lists[1]


# In[ ]:


# Grab first item of the first item in the matrix object
list_of_lists[1]


# In[ ]:


list_of_lists[1][1][][][]


# In[ ]:




