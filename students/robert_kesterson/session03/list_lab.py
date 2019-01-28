#!/usr/bin/env python3

# -------------------------------------------- #
# Title: Lesson 03 Exercise: List Lab
# Desc: This is a lab where we will learn about list manipulation
# Change log: (who, when, what)
# RKesterson, 2019-01-27, Created file
# RKestesron, 2019-01-27, Stubbed out methods / parts
# RKesterson, 2019-01-27, Completed series one (question about this to be posted to forum)
# RKesterson, 2019-01-XX, Completed series two 
# RKesterson, 2019-01-XX, Completed series three
# RKesterson, 2019-01-XX, Completed series four
# ---------------------------------------------- #

# Series one
listSeriesOne = ["Apples", "Pears", "Oranges", "Peaches"]
print(listSeriesOne)
response = input("Choose a fruit to add to the list: ")
listSeriesOne.append(response)
print(listSeriesOne)
response = input("Select a fruit by number: ")
fruitSelection = int(response)
print("Fruit number " + response + " - " + listSeriesOne[fruitSelection - 1])
# listSeriesOne[0]
#print(listSeriesOne)
listSeriesOne.insert(0, "Strawberries")
print(listSeriesOne)

# Series two

# Series three

# Series four