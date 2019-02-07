#!/usr/bin/env python3

# -------------------------------------------- #
# Title: Lesson 05 Exercise: Exceptions
# Desc: Improve your mailroom by adding exceptions and comprehensions.
# Change log: (who, when, what)
# RKesterson, 2019-02-06, Copied file to session05 dir
# Note - Commit to FebUpdates branch when creating pull request this week
# ---------------------------------------------- #

"""
silly little test module that is designed to trigger Exceptions when
run from the except_exercise.py file
"""

import time

conclude = "And what leads you to that conclusion?"
district = "Finest in the district, sir."
cheese = "It's certainly uncontaminated by cheese."
clean = "Well, it's so clean."
shop = "Not much of a cheese shop really, is it?"
cust = "Customer: "
clerk = "Shopkeeper: "


def fun(reaper):
    if reaper == 'spam':
        print(s)
    elif reaper == 'cheese':
        print()
        print('Spam, Spam, Spam, Spam, Beautiful Spam')
    elif reaper == 'mr death':
        print()
        return('{}{}\n{}{}'.format(cust, shop, clerk, district))


def more_fun(language):
    if language == 'java':
        test = [1, 2, 3]
        test[5] = language
    elif language == 'c':
        print('{}{}\n{}{}'.format(cust, conclude, clerk, clean))


def last_fun():
    print(cust, cheese)
    time.sleep(1)
    import antigravity
