#!/usr/bin/python

# -------------------------------------------- #
# Title: Lesson 05 Exercise: Exceptions
# Desc: Improve your mailroom by adding exceptions and comprehensions.
# Change log: (who, when, what)
# RKesterson, 2019-02-06, Copied file to session05 dir
# RKesterson, 2019-02-12, Began debugging exercise
# RKesterson, 2019-02-12, Completed debugging exercise
# Note - Commit to FebUpdates branch when creating pull request this week
# ---------------------------------------------- #

"""
An exercise in playing with Exceptions.
Make lots of try/except blocks for fun and profit.

Make sure to catch specifically the error you find, rather than all errors.
"""

from except_test import fun, more_fun, last_fun


# Figure out what the exception is, catch it and while still
# in that catch block, try again with the second item in the list
first_try = ['spam', 'cheese', 'mr death']

try:
    joke = fun(first_try[0])
except NameError as the_error:
    joke = fun(first_try[1])
    # print(the_error)

# Here is a try/except block. Add an else that prints not_joke
try:
    not_joke = fun(first_try[2])
except SyntaxError:
    print('Run Away!')
else:
    print(not_joke)

# What did that do? You can think of else in this context, as well as in
# loops as meaning: "else if nothing went wrong"
# (no breaks in  loops, no exceptions in try blocks)

# Figure out what the exception is, catch it and in that same block
#
# try calling the more_fun function with the 2nd language in the list,
# again assigning it to more_joke.
#
# If there are no exceptions, call the more_fun function with the last
# language in the list

# Finally, while still in the try/except block and regardless of whether
# there were any exceptions, call the function last_fun with no
# parameters. (pun intended)

langs = ['java', 'c', 'python']

try:
    more_joke = more_fun(langs[0])
except IndexError:
    more_joke = more_fun(langs[1])
else:
    more_fun(langs[2])
finally:
    last_fun()
