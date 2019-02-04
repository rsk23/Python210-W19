#!/usr/bin/env python3

# -------------------------------------------- #
# Title: Lesson 04 Activities: Dictionary and Set Lab
# Desc: Learn the basic ins and outs of Python dictionaries and sets.
# Change log: (who, when, what)
# RKesterson, 2019-01-30, Created file
# RKestesron, 2019-01-30, Stubbed out methods / parts
# RKestesron, 2019-02-03, Completed dictionaries

# Note - Commit to FebUpdates branch when creating pull request this week
# ---------------------------------------------- #

# Dictionaries
dictOne = {
    'name': 'Chris',
    'city': 'Seattle',
    'cake': 'Chocolate'
}
for i in dictOne.keys():
    print("Key: {:s} | Value: {:s}".format(i, dictOne[i]))

del dictOne['cake']
for i in dictOne.keys():
    print("{:s}: {:s}".format(i, dictOne[i]))

dictOne['fruit'] = 'Mango'
print(dictOne.keys())
print(dictOne.values())
print('cake' in dictOne)
print('Mango' in dictOne.values())

# Dictionaries 2


# Sets

# Sets 2