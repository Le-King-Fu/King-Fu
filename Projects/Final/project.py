from os.path import exists
import csv
import sys
import tabulate
import datetime
import os

absolute_path = os.path.dirname(__file__)
#relative_path = "Count_Me_One"
#full_path = os.path.join(absolute_path, relative_path)


activity_header = ['name', 'description', 'unit']
activity_unit = ["kilometers", "units", "minutes", "hours"]
activity_csv = str(absolute_path + "/activity.csv")
activity_csv_temp = str(absolute_path + "/temp_activity.csv")
entry_header = ['date', 'activity', 'qtt']
entry_csv = str(absolute_path + "/log.csv")
menu_intro = ["1","2","3","4","x"]
menu_choice = str(
"""
Welcome ! Please pick a number :
    1 - Show activities
    2 - Edit activities
    3 - Add entry
    4 - Show entries
    X - Exit
Input: """
)
menu_choice2 = str(
"""
Please try again (make sure you input a number):
    1 - Show activities
    2 - Edit activities
    3 - Add entry
    4 - Show entries
Input: """)
menu_activity = ["1","2","3","x"]
choice_activity = str(
"""
Pick a number :
1 - Add an activity
2 - Edit an activity
3 - Remove an activity
x - Back to home menu
Input: """
)

def main():
    while True:
        n = intro()
        if n == "1":
            validate_file_activity()
            activity_print()
        elif n == "2":
            validate_file_activity()
            activity_edit()
        elif n == "3":
            entry_input()
        elif n == "4":
            entry_print()
        else:
            sys.exit("Bye")

def intro():
    n = input(menu_choice).lower()
    if n not in menu_intro:
        while n not in menu_intro:
            n = input(menu_choice2)
    return n

def activity_edit():
    n = input(choice_activity).lower()
    if n not in menu_activity:
        while n not in menu_activity:
            n = input(choice_activity)

    if n == "1":
        activity_info = get_activity_info()
        activity_add(*activity_info)

#edit an activity
    elif n == "2":
        activity_remove(name_input())
        print("Please enter new values...")
        activity_add()

#remove a line
    elif n == "3":
        activity_remove(name_input())

    else:
        main()

def get_activity_info():
    name = input("Name: ")
    description = input("Description: ")
    unit_id = unit_type_input()  # unit_type_input is a function that prompts the user to choose a unit and returns the unit ID
    return name, description, unit_id

def activity_add(name, description, unit_id):
    while name_validate(name):
        name = input("Already exist. Choose another name: ")
    with open(activity_csv, 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow([name, description, activity_unit[unit_id-1]])
        f.close()

def activity_remove(name):
    with open(activity_csv, 'r') as inp, open(activity_csv_temp, 'w') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if row[0] != name:
                writer.writerow(row)
    with open(activity_csv, 'w') as out, open(activity_csv_temp, 'r') as inp:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            writer.writerow(row)

def activity_print():
    activities = []
    validate_file_activity()
    with open(activity_csv, encoding='UTF8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            activities.append({"Name": row["name"], "Description": row["description"], "Unit": row["unit"]})
        print(tabulate.tabulate(activities, headers="keys", tablefmt='grid'))

def entry_print():
    entries = []
    validate_file_entry()
    with open(entry_csv, encoding='UTF8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            entries.append({"Date": row["date"], "Activity": row["activity"], "Quantity": row["qtt"]})
        print(tabulate.tabulate(entries, headers="keys", tablefmt='grid'))

def entry_input():
    entry_name = name_input()
    with open(activity_csv, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if entry_name == row["name"]:
                entry_unit = row["unit"]
    entry_qtt = input(f"How many {entry_unit} ?")
    validate_file_entry()
    with open(entry_csv, 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.datetime.now(), entry_qtt, entry_name])
        f.close()

def unit_type_input():
    print("Type of unit : ")
    for (i, unit) in enumerate(activity_unit, start=1):
        print(i, " - ", unit)
    unit_id = int(input("Input the number: "))
    return unit_id

def name_input():
    name_input = " "
    while name_validate(name_input) is False:
        print("What activity ? ")
        activity_print()
        name_input = input("Name: ")
    return name_input

def name_validate(name):
    with open(activity_csv, encoding='UTF8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if name == row["name"]:
                return True
        return False

def validate_file_activity():
    #path = ""
    if exists(activity_csv):
        pass
    else:
        print("initializing list...")
        with open(activity_csv, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(activity_header)
            f.close()

def validate_file_entry():
    #path = ""
    if exists(entry_csv):
        pass
    else:
        print("initializing log...")
        with open(entry_csv, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(entry_header)
            f.close()

if __name__ == "__main__":
    main()
