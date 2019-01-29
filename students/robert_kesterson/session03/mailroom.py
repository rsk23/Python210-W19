#!/usr/bin/env python3

# -------------------------------------------- #
# Title: Lesson 03 Exercise: Mailroom, part 1
# Desc: First major assignment
# Change log: (who, when, what)
# RKesterson, 2019-01-29, Created file
# RKestesron, 2019-01-29, Stubbed out methods / parts
# RKesterson, 2019-01-29, Started task one
# ---------------------------------------------- #

response = input("Choose an action: Send a Thank You, Create a Report, quit")
if response == "Send a Thank You":
    #Add code here
if response == "Create a Report":
    #Add code here
if response == "quit":
    #Add code here
while response != "Send a Thank You" and response != "Create a Report" and response != "quit":
    response = input("You must chose an action from the approved list. Actions are: Send a Thank you, "
                     "Create a Report, quit")