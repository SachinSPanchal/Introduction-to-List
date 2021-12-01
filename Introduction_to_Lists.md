### Earlier when discussing strings we introduced the concept of a <u>sequence</u> in Python. 
* <u>Lists</u> can be thought of the most general version of a *sequence* in Python. 


* Unlike strings, they are mutable, meaning the elements inside a list can be changed! 


* Lists are constructed with brackets <code>[]</code> and commas separating every element in the list.


```python
# Assign a list to an variable named my_list
my_list = [1,2,3,4]
```


```python
print(my_list)
```

    [1, 2, 3, 4]
    


```python
type(my_list)
```




    list



* We just created a list of integers, but lists can actually hold different object types. For example:


```python
my_list = ['A string',23,100.232,'o',True]
```


```python
my_list
```




    ['A string', 23, 100.232, 'o', True]



* Just like strings, the <code>len()</code> function will tell you how many items are in the sequence of the list.


```python
len(my_list)
```




    5



## List Indexing
* Indexing work just like in strings.


* A list index refers to the location of an element in a list.


* Remember the indexing begins from 0 in Python. 


* The first element is assigned an index 0, the second element is assigned an index of 1 and so on and so forth.


```python
# Consider a list of strings
loss_functions = ['Mean Absolute Error','Mean Squared Error','Huber Loss','Log Loss','Hinge Loss']
print(loss_functions)
```

    ['Mean Absolute Error', 'Mean Squared Error', 'Huber Loss', 'Log Loss', 'Hinge Loss']
    


```python
# Grab the element at index 0, which is the FIRST element
print(loss_functions[0])
```

    Mean Absolute Error
    


```python
len(loss_functions)
```




    5




```python
# Grab the element at index 3, which is the FOURTH element
print(loss_functions[3])
```

    Log Loss
    


```python
print(loss_functions[6])
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-11-36fa04b37479> in <module>()
    ----> 1 print(loss_functions[6])
    

    IndexError: list index out of range



```python
# Grab the element at the index -1, which is the LAST element
print(loss_functions[-1])
```

    Hinge Loss
    


```python
# Grab the element at the index -3, which is the THIRD LAST element
print(loss_functions[-3])
```

    Huber Loss
    

## List Slicing

* We can use a <code>:</code> to perform *slicing* which grabs everything up to a designated point. 


* The starting index is specified on the left of the <code>:</code> and the ending index is specified on the right of the <code>:</code>. 


* Remember the element located at the right index is not included.


```python
# Print our list
print(loss_functions)
```

    ['Mean Absolute Error', 'Mean Squared Error', 'Huber Loss', 'Log Loss', 'Hinge Loss']
    


```python
# Grab the elements starting from index 1 and everything past it
loss_functions[1:4]
```




    ['Mean Squared Error', 'Huber Loss', 'Log Loss']



* If you do not specify the ending index, then all elements are extracted which comes after the starting index including the element at that starting index. The operation knows only to stop when it has run through the entire list.


```python
# Grab everything starting from index 2
loss_functions[2:]
```




    ['Huber Loss', 'Log Loss', 'Hinge Loss']



* If you do not specify the starting index, then all elements are extracted which comes befores the ending index excluding the element at the specified ending index. The operation knows only to stop when it has extracted all elements before the  element at the ending index.


```python
# Grab everything before the index 4
loss_functions[:4]
```




    ['Mean Absolute Error', 'Mean Squared Error', 'Huber Loss', 'Log Loss']



* If you do not specify the starting and the ending index, it will extract all elements of the list.


```python
# Grab everything
print(loss_functions[:])
```

    ['Mean Absolute Error', 'Mean Squared Error', 'Huber Loss', 'Log Loss', 'Hinge Loss']
    

* We can also extract the last four elements. Remember we can use the index -4 to extract the FOURTH LAST element


```python
# Grab the LAST FOUR elements of the list
loss_functions[-4:]
```




    ['Mean Squared Error', 'Huber Loss', 'Log Loss', 'Hinge Loss']




```python
loss_functions[-10]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-20-8a581720341d> in <module>()
    ----> 1 loss_functions[-10]
    

    IndexError: list index out of range


* It should also be noted that list indexing will return an error if there is no element at that index.


```python
len(loss_functions)
```




    5




```python
loss_functions[8]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-21-4de3193e7629> in <module>()
    ----> 1 loss_functions[8]
    

    IndexError: list index out of range


## List Operations
* Remember we said that lists are mutable as opposed to strings. Lets see how can we change the elements of a list

* We can also use <code>+</code> to concatenate lists, just like we did for strings.


```python
print(loss_functions)
```

    ['Mean Absolute Error', 'Mean Squared Error', 'Huber Loss', 'Log Loss', 'Hinge Loss']
    


```python
loss_functions + ['Kullback-Leibler']
```




    ['Mean Absolute Error',
     'Mean Squared Error',
     'Huber Loss',
     'Log Loss',
     'Hinge Loss',
     'Kullback-Leibler']



* Note: This doesn't actually change the original list!


```python
print(loss_functions)
```

    ['Mean Absolute Error', 'Mean Squared Error', 'Huber Loss', 'Log Loss', 'Hinge Loss']
    

* You would have to reassign the list to make the change permanent.


```python
# Reassign
loss_functions = loss_functions + ['Kullback-Leibler']
```


```python
loss_functions
```




    ['Mean Absolute Error',
     'Mean Squared Error',
     'Huber Loss',
     'Log Loss',
     'Hinge Loss',
     'Kullback-Leibler']



* We can also use the <code>*</code> for a duplication method similar to strings:


```python
# Make the list double
len(loss_functions * 6)
```




    36



## List Functions

### <code>len()</code>


* <code>len()</code> function returns the length of the list


```python
print(loss_functions)
```

    ['Mean Absolute Error', 'Mean Squared Error', 'Huber Loss', 'Log Loss', 'Hinge Loss', 'Kullback-Leibler']
    


```python
len(loss_functions)
```




    6



### <code>min()</code>


* <code>min()</code> function returns the minimum element of the list


* <code>min()</code> function only works with lists of similar data types


```python
new_list = [6, 9, 1, 3, 5.5]
```


```python
min(new_list)
```




    1




```python
my_new_list = ['a','b', 'z' ,'y' , 'm']
```


```python
min(my_new_list)
```




    'a'



### <code>max()</code>


* <code>max()</code> function returns the maximum element of the list


* <code>max()</code> function only works with lists of similar data types


```python
new_list = ['Argue','Burglar','Parent','Linear','shape']
```


```python
max(new_list)
```




    'shape'



### <code>sum()</code>


* <code>sum()</code> function returns the sum of the elements of the list


* <code>sum()</code> function only works with lists of numeric data types


```python
new_list = [6, 9, 1, 3, 5.5]
```


```python
sum(new_list)
```




    24.5



### <code>sorted()</code>


* <code>sorted()</code> function returns the sorted list 


* <code>sorted()</code> function takes reverse boolean as an argument


* <code>sorted()</code> function only works on a list with similar data types


```python
new_list
```




    [6, 9, 1, 3, 5.5]




```python
sorted(new_list)
```




    [1, 3, 5.5, 6, 9]




```python
print(new_list)
```

    [6, 9, 1, 3, 5.5]
    


```python
new_list = ['Argue','Burglar','Parent','Linear','shape']
```


```python
sorted(new_list)
```




    ['Argue', 'Burglar', 'Linear', 'Parent', 'shape']




```python
print(new_list)
```

    [6, 9, 1, 3, 5.5]
    


```python
sorted(new_list,reverse=True)
```




    [9, 6, 5.5, 3, 1]




```python
sorted(new_list)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-45-99e16da477d4> in <module>()
    ----> 1 sorted(new_list,False)
    

    TypeError: sorted expected 1 arguments, got 2


* <code>sorted()</code> function does not change our list


```python
new_list
```




    [6, 9, 1, 3, 5.5]



## List Methods

* If you are familiar with another programming language, you might start to draw parallels between arrays in another language and lists in Python. Lists in Python however, tend to be more flexible than arrays in other languages for a two good reasons: they have no fixed size (meaning we don't have to specify how big a list will be), and they have no fixed type constraint (like we've seen above).


* Let's go ahead and explore some more special methods for lists:


```python
# Create a new list
my_list = [1,2,3,1,1,1,3,10,5,8]
```

### <code>append()</code> 

* Use the <code>append()</code> method to permanently add an item to the end of a list.


* <code>append()</code> method takes the element which you want to add to the list as an argument


```python
# Print the list
my_list
```




    [1, 2, 3, 1, 1, 1, 3, 10, 5, 8]




```python
len(my_list)
```




    10




```python
# Append to the end of the list
my_list.append('Append me!')
```

* Ah darn it! I was expecting some output. Lets see what happened to <code>my_list</code>


```python
print(my_list)
```

    [1, 2, 3, 1, 1, 1, 3, 10, 5, 8, 'Append me!']
    


```python
len(my_list)
```




    11



* Woah! Calling the <code>append()</code> method changed my list? Yes, the <code>append()</code>  method changes your original list!


```python
# Show
my_list.append(2.73)
```


```python
print(my_list)
```

    [1, 2, 3, 1, 1, 1, 3, 10, 5, 8, 'Append me!', 2.73]
    

* We can in fact add a list object to our <code>my_list</code> object


```python
my_list.append([1,2,3])
```


```python
my_list
```




    [1, 2, 3, 1, 1, 1, 3, 10, 5, 8, 'Append me!', 2.73, [1, 2, 3]]




```python
len(my_list)
```




    13




```python
my_list.append([10,[19,20],30])
```


```python
len(my_list)
```




    14



### <code>extend()</code>

* Use the <code> extend()</code> method to merge a list to an existing list


* <code> extend()</code> method takes a list or any iterable(don't worry about it now) as an argument.


* Quite helpful when you have two or more lists and you want to merge them together


```python
# Print the list
print(my_list)
```

    [1, 2, 3, 1, 1, 1, 3, 10, 5, 8, 'Append me!', 2.73, [1, 2, 3], [10, [19, 20], 30]]
    


```python
my_list.extend(['Wubba','Lubba','Dub Dub'])
```


```python
print(my_list)
```

    [1, 2, 3, 1, 1, 1, 3, 10, 5, 8, 'Append me!', 2.73, [1, 2, 3], [10, [19, 20], 30], 'Wubba', 'Lubba', 'Dub Dub']
    


```python
len(my_list)
```




    17



### <code>pop()</code>

* Use <code>pop()</code> to "pop off" an item from the list. 


* By default <code>pop()</code> takes off the element at the last index, but you can also specify which index to pop off. 


* <code>pop()</code> takes the index as an argument and returns the elenent which was popped off.


```python
# Print the list
print(my_list)
```

    [1, 2, 3, 1, 1, 1, 3, 10, 5, 8, 'Append me!', 2.73, [1, 2, 3], [10, [19, 20], 30], 'Wubba', 'Lubba', 'Dub Dub']
    


```python
# Pop off the 0 indexed item
my_list.pop()
```




    'Dub Dub'



* <code>pop()</code> method changes the list by popping off the element at the specified index


```python
print(my_list)
```

    [1, 2, 3, 1, 1, 1, 3, 10, 5, 8, 'Append me!', 2.73, [1, 2, 3], [10, [19, 20], 30], 'Wubba', 'Lubba']
    


```python
# Assign the popped element, remember default popped index is -1
my_list.pop(-1)
```




    'Lubba'




```python
len(my_list)
```




    14




```python
print(my_list)
```

    [1, 2, 3, 1, 1, 1, 3, 10, 5, 8, 'Append me!', 2.73, [1, 2, 3], [10, [19, 20], 30], 'Wubba']
    

### <code>remove()</code>

* Use <code>remove()</code> to remove an item/element from the list. 


* By default <code>remove()</code> removes the specified element from the list.


* <code>remove()</code> takes the element as an argument.


```python
# Print the list
print(my_list)
```

    [1, 2, 3, 1, 1, 1, 3, 10, 5, 8, 'Append me!', 2.73, [1, 2, 3], [10, [19, 20], 30], 'Wubba']
    


```python
# Remove the element which you want to 
my_list.remove([10, [19, 20], 30])
```


```python
# Show
print(my_list)
```

    [1, 2, 3, 1, 1, 1, 3, 10, 5, 8, 'Append me!', 2.73, [1, 2, 3], 'Wubba']
    


```python
my_list.remove([1,2,3])
```


```python
print(my_list)
```

    [1, 2, 3, 1, 1, 1, 3, 10, 5, 8, 'Append me!', 2.73, 'Wubba']
    


```python
len(my_list)
```




    12




```python
my_list.remove(1)
```


```python
print(my_list)
```

    [2, 3, 1, 1, 3, 10, 5, 8, 1.43, 'Wubba', 'Lubba']
    


```python
len(my_list)
```




    11




```python
my_list.clear
```

### <code>count()</code>


* The <code>count()</code> method returns the total occurrence of a specified element in the list


```python
print(my_list)
```

    [1, 2, 3, 1, 1, 1, 3, 10, 5, 8, 'Append me!', 2.73, 'Wubba']
    


```python
# Count the number of times element 1 occurs in my_list
my_list.count('Wubba')
```




    1




```python
my_list.count(1)
```




    4



### <code>index()</code>


* The <code>index()</code> method returns the index of a specified element.


```python
print(my_list)
```

    [1, 2, 3, 1, 1, 1, 3, 10, 5, 8, 'Append me!', 2.73, 'Wubba']
    


```python
my_list.index('Wubba')
```




    12




```python
my_list.index(3)
```




    2



### <code>sort()</code>

* Use <code>sort()</code> to sort the list in either ascending/descending order


* The sorting is done in ascending order by default


* <code>sort()</code> method takes the reverse boolean as an argument


* <code>sort()</code> method only works on a list with elements of same data type


```python
new_list = [6, 9, 1, 3, 5]
```


```python
# Use sort to sort the list (this is permanent!)
new_list.sort()
```


```python
print(new_list)
```

    [1, 3, 5, 6, 9]
    


```python
# Use the reverse boolean to set the ascending or descending order
new_list.sort(reverse=True)
print(new_list)
```

    [9, 6, 5, 3, 1]
    


```python
boolean_list = [True, False]
```


```python
boolean_list.sort(reverse=True)
```


```python
print(boolean_list)
```

    [True, False]
    

### <code>reverse()</code>

* <code>reverse()</code> method reverses the list


```python
my_list = [1, 1, 1, 1, 1.43, 2, 3, 3, 5, 8, 10, 'Lubba', 'Dub Dub']
```


```python
print(my_list)
```

    [1, 1, 1, 1, 1.43, 2, 3, 3, 5, 8, 10, 'Lubba', 'Dub Dub']
    


```python
my_list.reverse()
```


```python
print(my_list)
```

    ['Dub Dub', 'Lubba', 10, 8, 5, 3, 3, 2, 1.43, 1, 1, 1, 1]
    

## Nested Lists

* A great feature of of Python data structures is that they support *nesting*. This means we can have data structures within data structures. For example: A list inside a list.


```python
# Let's make three lists
lst_1=[1,2,3]
lst_2=['b','a','d']
lst_3=[7,8,9]

# Make a list of lists to form a matrix
list_of_lists = [lst_1,lst_2,lst_3]
```


```python
print(list_of_lists)
```

    [[1, 2, 3], ['b', 'a', 'd'], [7, 8, 9]]
    


```python
# Show
type(list_of_lists)
```




    list




```python
# Grab first item in matrix object
list_of_lists[1]
```




    ['b', 'a', 'd']




```python
# Grab first item of the first item in the matrix object
list_of_lists[1]
```




    ['b', 'a', 'd']




```python
list_of_lists[1][1][][][]
```




    'a'




```python

```
