#!/usr/bin/env python3

# -------------------------------------------- #
# Title: Lesson 05 Assignment: Mailroom, Part 3
# Desc: Improve your mailroom by adding exceptions and comprehensions.
# Change log: (who, when, what)
# RKesterson, 2019-02-06, Created file
# RKesterson, 2019-02-12, Added code from mailroompart2.py
#
# RKesterson, 2019-02-12, Added try / catch (try / except) blocks for user input
# RKesterson, 2019-02-12, Added comprehensions to process a sequence of items to create another sequence
# Note - Commit to FebUpdates branch when creating pull request this week
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

def send_thank_you():
    global donationdict
    tyresponse = input("Please enter a full name. list provides all names")
    while True:
        if tyresponse == "list":
            for i in donationdict.keys():
                print("{:s}".format(i))
            tyresponse = input("Please enter a full name. List provides all names")
        else:
            donation = input("Enter a donation amount")
            donation = int(donation)
            if tyresponse in donationdict.keys():
                donvalue = donationdict[tyresponse]
                donvalue.append(donation)
                donationdict[tyresponse] = donvalue
            else:
                donvalue = []
                donvalue.append(donation)
                donationdict[tyresponse] = donvalue
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