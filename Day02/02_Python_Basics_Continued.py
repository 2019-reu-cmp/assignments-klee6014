# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:41:24 2019

@author: Kinsey Lee
02: Python Basics Continued
"""

""" 1)  How many bisections do you expect to need if the tolerance is 10−3?
         10−6? 10−9? Explain your reasoning.
"""

""" I expect 10 iterations for a tolerance of 10**-3. I expect 20 iterations
for a tolerance of 10**-6, and 30 for a tolerance of 10**-9. Tolerance is the
tolerable error in the approximation via the bisection method. The lower 
tolerance, the smaller the width of the sections for the bisection method, and,
thus, more iterations."""


""" 2)How (aside from actually changing the function in the code) could you 
        make bisection.py easier to use for diﬀerent functions?
"""
        
""" You could make all the code below the f(x) function its own function with
parameters for xa, xb, and tolerance. (All other variables can be locally
determined.) Then the function could return the new xa and xb as well as 
iteration_count. """


""" 3)  What are the diﬀerences between lists and tuples? Tuples and 
        dictionaries? Sets and dictionaries? In what cases might you use each?
"""

""" lists v. tuples:
    Lists are indicated by square brackets. Tuples are indicated by parentheses.
    You can edit the length of a list as well as its values. This isn't
    possible with tuples.
    
    Tuples v. dictionaries:
    Tuples are indicated by square brackets. Dictionaries are indicated by
    curly brackets. Tuples are essentially like dictionaries whose keys are 
    sequential integers from zero. You do not need to indicate keys in a tuple.
    Because tuples have a set code for their keys, they cannot be re-ordered.
    Order does not matter in a dictionary as long as each key is present.
    
    sets v. dictionaries
    Sets are indicated by 'set([])'. Dictionaries are indicated by curly
    brackets. Dictionaries have set keys that impose some sense of order in the
    dictionary. Sets are unordered and unindexed.
    
    Lists are useful when you might want indexes, but you might want to change
    the list while the function runs.
    
    Tuples are useful if you have a set of values that will remain constant
    throughout the code.
    
    Dictionaries are helpful if you don't want to use purely integer indicies
    to refer to the elements of the dictionary. They are also helpful if you
    do not want the elements to be tied together sequentially.
    
    Sets are useful if your elements don't need to elements to be in an order.
"""


""" 4)  How would you check within an if statement if a variable is a list or
    not? Why would you need to do this?
"""
    
""" The conditional I would use to determine whether or not the variable is a 
list is 'if (type(variable) == list):'. If the type of the variable were equal 
to a list you could proceed with coding that only applies to list. You would 
need to do this if you wanted to change the values kept in the indices or if 
you wanted to change the size of the elements in the variable."""
