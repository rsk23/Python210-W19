#!/usr/bin/env python3

# -------------------------------------------- #
# Title: Lesson 04 Assignment: Mailroom, Part 2
# Desc: Incorporate file writing and dictionary use.
# Change log: (who, when, what)
# RKesterson, 2019-01-30, Created file
# RKestesron, 2019-02-05, Stubbed out methods / parts
# RKestesron, 2019-02-05, Updated code to use a dict to switch between the user’s selections

# RKestesron, 2019-02-05, Converted main donor data structure to be a dict
# RKestesron, 2019-02-05, Updated code to produce the letter as one big template, rather than building up a
# big string that produces the letter in parts
# RKestesron, 2019-02-05, Added "send letters to all donors" feature
# RKestesron, 2019-02-05, Updated "send letter to all donors" feature to write to files in working dir

# Note - Commit to FebUpdates branch when creating pull request this week
# ---------------------------------------------- #

donationlist = []

def load_donation_list():
    global donationlist
    firstdonation = ("Winston Churchill", 2)
    donationlist.append(firstdonation)
    firstdonation = ("Winston Churchill", 20)
    donationlist.append(firstdonation)
    firstdonation = ("Hunter S. Thompson", 50)
    donationlist.append(firstdonation)
    firstdonation = ("Hunter S. Thompson", 500)
    donationlist.append(firstdonation)
    firstdonation = ("Hunter S. Thompson", 5000)
    donationlist.append(firstdonation)
    firstdonation = ("Richard Garfield", 300)
    donationlist.append(firstdonation)
    firstdonation = ("Richard Garfield", 400)
    donationlist.append(firstdonation)
    firstdonation = ("Simon Illyan", 100)
    donationlist.append(firstdonation)
    firstdonation = ("Theodore Roosevelt", 50)
    donationlist.append(firstdonation)
    firstdonation = ("Theodore Roosevelt", 100)
    donationlist.append(firstdonation)

def send_thank_you():
    global donationlist
    tyresponse = input("Please enter a full name. list provides all names")
    while True:
        if tyresponse == "list":
            donationlist.sort()
            namelist = ""
            for tupleobject in donationlist:
                if tupleobject[0] not in namelist and namelist == "":
                    namelist = namelist + "{:s}".format(tupleobject[0])
                elif tupleobject[0] not in namelist:
                    namelist = namelist + ",{:s}".format(tupleobject[0])
            print(namelist)
            tyresponse = input("Please enter a full name. List provides all names")
        else:
            donation = input("Enter a donation amount")
            donation = int(donation)
            newdonation = (tyresponse, donation)
            print("Thank you {:s} for your generous donation of {:d} dollars".format(newdonation[0], newdonation[1]))
            donationlist.append(newdonation)
            break

def create_a_report():
    i = 1
    reportlist = []
    currentname = ""
    totalgiven = 0
    numberofgifts = 0
    donationlist.sort()
    # If the currentname is the empty set, we have not started to iterate yet
    for tupleobject in donationlist:
        if currentname == "":
            currentname = tupleobject[0]
            totalgiven = tupleobject[1]
            numberofgifts = 1
        # If we encounter a different name from the current name, we know we have reached a new donor
        elif currentname != tupleobject[0]:
            reporttuple = (totalgiven, currentname, numberofgifts)
            reportlist.append(reporttuple)
            currentname = tupleobject[0]
            totalgiven = tupleobject[1]
            numberofgifts = 1
        # If we encounter the same name, we want to add to the information about said donor
        else:
            totalgiven += tupleobject[1]
            numberofgifts += 1

    # Now that the tuples are totaled, we can sort and print them
    reportlist.sort()
    reportlist.reverse()
    for tupleobject in reportlist:
        print("{:s} {:d} {:d}")

def break_function():
    exit()

def send_letters_to_all_donors():
    return

def load_selection_list():
    switch_function_dict = {
        '1 - Send a Thank You to a single donor.': send_thank_you,
        '2 - Create a Report.': create_a_report,
        '3 - Send letters to all donors.': send_letters_to_all_donors,
        '4 - Quit': break_function
    }
    return switch_function_dict

if __name__ == '__main__':
    switch_function_dict = load_selection_list()
    # switch_function_dict = load_donation_list()
    # response = input("Choose an action: Send a Thank You, Create a Report, quit")

    while True:
        print("Chose an action: \r\n")
        for i in switch_function_dict.keys():
            print("{:s}".format(i))
        response = input("")
        # response = int(response)
        if response not in switch_function_dict.keys():
            print("You must chose an action from the approved list. Actions are: \r\n")
            for i in switch_function_dict.keys():
                print("{:s}".format(i))
            response = input("")
        else:
            # switch_function_dict[response]
            switch_function_dict.get(response)()
