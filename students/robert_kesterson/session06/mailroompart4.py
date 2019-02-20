#!/usr/bin/env python3

# -------------------------------------------- #
# Title: Lesson 06 Assignment: Mailroom, Part 4
# Desc: Add a full suite of unit tests.
# Change log: (who, when, what)
# RKesterson, 2019-02-13, Created file
# RKestesron, 2019-02-16, Copied over content from mailroompart3
# RKestesron, 2019-02-16, Realized I didn't need a separate file for unit tests lol
# RKestesron, 2019-02-16, Refactored load_donation_dict code to better support unit tests
# RKestesron, 2019-02-16, Refactored send_thank_you to support better unit tests
# RKestesron, 2019-02-16, Added add_donation to support better unit tests
# ---------------------------------------------- #

donationdict = {}

def load_donation_dict():
    global donationdict
    donationdict = {
        'Winston Churchill': [20, 50],
        'Hunter S. Thompson': [50, 500, 5000],
        'Richard Garfield': [300, 400],
        'Simon Illyan': [100],
        'Theodore Roosevelt': [50, 100]
    }
    return donationdict

def add_donation(donorname, dollaramount):
    global donationdict
    if donorname in donationdict.keys():
        donvalue = donationdict[donorname]
        donvalue.append(dollaramount)
        donationdict[donorname] = donvalue
    else:
        donvalue = []
        donvalue.append(dollaramount)
        donationdict[donorname] = donvalue

def send_thank_you():
    global donationdict
    tyresponse = input("Please enter a full name. list provides all names")
    while True:
        if tyresponse == "list":
            for i in donationdict.keys():
                print("{:s}".format(i))
            tyresponse = input("Please enter a full name. List provides all names")
        else:
            donation = input("Enter a donation amount as a whole dollar integer value.")
            try:
                donation = int(donation)
            except ValueError:
                print("Input must be an integer. Try again")
                break
            add_donation(tyresponse, donation)
            print("Thank you {:s} for your generous donation of {:d} dollars".format(tyresponse, donation))
            break

def sort_key(donor):
    return donor[1]

def create_a_report():
    donationlist = []
    for i in donationdict.keys():
        donationcount = 0
        donationtotal = 0
        donationvalue = donationdict[i]
        for j in donationvalue:
            donationtotal += int(j)
            donationcount += 1
        averagedonation = donationtotal / donationcount
        tupleone = (i, donationtotal, donationcount, averagedonation)
        donationlist.append(tupleone)
    sorteddonorlist = sorted(donationlist, key=sort_key)
    sorteddonorlist.reverse()
    print("Donor Name | Total Given | Num Gifts | Average Gift")
    print("---------------------------------------------------")
    for k in sorteddonorlist:
        print("{:s} ${:d} {:d} ${:.2f}".format(k[0], k[1], k[2], k[3]))

def break_function():
    exit()

def send_letters_to_all_donors():
    global donationdict
    for i in donationdict.keys():
        filename = "{:s}.txt".format(i)
        outfile = open(filename, 'w')
        donationtotal = 0
        donationvalue = donationdict[i]
        for j in donationvalue:
            donationtotal += int(j)
        messagestring = "Dear {:s}, \r\n\n    Thank you for your very kind donation of ${:d}.\r\n\n    It will be put" \
                        " to very good use.\r\n\n            Sincerely,\r\n                -The Team".format(i, donationtotal)
        outfile.write(messagestring)
        outfile.close()

def load_selection_list():
    switch_function_dict = {
        '1 - Send a Thank You to a single donor.': send_thank_you,
        '2 - Create a Report.': create_a_report,
        '3 - Send letters to all donors.': send_letters_to_all_donors,
        '4 - Quit': break_function
    }
    return switch_function_dict
'''
if __name__ == '__main__':
    switch_function_dict = load_selection_list()
    load_donation_dict()

    while True:
        print("Chose an action: \r\n")
        for i in switch_function_dict.keys():
            print("{:s}".format(i))
        response = input("")
        if response not in switch_function_dict.keys():
            print("You must chose an action from the approved list. Actions are: \r\n")
            for i in switch_function_dict.keys():
                print("{:s}".format(i))
            response = input("")
        else:
            switch_function_dict.get(response)()
'''
# Begin by testing the core logic needed to create the data structure that the mailroom code depends on
try:
    print("Beginning by checking if the dict data structure (and associated content) properly loads when initialized")
    beginDict = load_donation_dict()

    if len(beginDict.keys()) == 5:
        print("Pass - Initial data structure has the correct number of keys")
    else:
        print("Fail - Initial data structure does not have the expected number of keys")

except Exception:
    print("{:s}".format(Exception))

# Next, verify that we have the ability to add to the core data structure
try:
    print("Now testing add_donation function.")
    print("First we will verify that adding a new unqiue name should cause the dict to add a key.")
    add_donation('Ringo Star', 25)
    if len(beginDict.keys()) == 6:
        print("Pass - We have successfully added a key")
    else:
        print("Fail - Did not add a key as expected")

    print("We will now add a donation with with a previously known name. The dict should not add a key.")
    add_donation('Winston Churchill', 25)
    if len(beginDict.keys()) == 6:
        print("Pass - Adding a donation for a known name did not add a new key")
    else:
        print("Fail - A new key was added when it should not have been")

except Exception:
    print("{:s}".format(Exception))