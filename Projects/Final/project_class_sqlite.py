import os
import csv
import tabulate
from os.path import exists
import datetime
import sys

class ActivityTracker:
    def __init__(self):
        self.absolute_path = os.path.dirname(__file__)
        self.activity_header = ['name', 'description', 'unit']
        self.activity_unit = ["kilometers", "units", "minutes", "hours"]
        self.activity_csv = str(self.absolute_path + "/activity.csv")
        self.activity_csv_temp = str(self.absolute_path + "/temp_activity.csv")
        self.entry_header = ['date', 'activity', 'qtt']
        self.entry_csv = str(self.absolute_path + "/log.csv")
        self.menu_intro = ["1","2","3","4","x"]
        self.menu_choice = str(
        """
        Welcome ! Please pick a number :
            1 - Show activities
            2 - Edit activities
            3 - Add entry
            4 - Show entries
            X - Exit
        Input: """
        )
        self.menu_choice2 = str(
        """
        Please try again (make sure you input a number):
            1 - Show activities
            2 - Edit activities
            3 - Add entry
            4 - Show entries
        Input: """)
        self.menu_activity = ["1","2","3","x"]
        self.choice_activity = str(
        """
        Pick a number :
        1 - Add an activity
        2 - Edit an activity
        3 - Remove an activity
        x - Back to home menu
        Input: """
        )

    def main(self):
        while True:
            n = self.intro()
            if n == "1":
                self.validate_file_activity()
                self.activity_print()
            elif n == "2":
                self.validate_file_activity()
                self.activity_edit()
            elif n == "3":
                self.entry_input()
            elif n == "4":
                self.entry_print()
            else:
                sys.exit("Bye")

    def intro(self):
        n = input(self.menu_choice).lower()
        if n not in self.menu_intro:
            while n not in self.menu_intro:
                n = input(self.menu_choice2)
        return n

    def activity_edit(self):
        n = input(self.choice_activity).lower()
        if n not in self.menu_activity:
            while n not in self.menu_activity:
                n = input(self.choice_activity)

        if n == "1":
            activity_info = self.get_activity_info()
            self.activity_add(*activity_info)

    #edit an activity
        elif n == "2":
            self.activity_remove(self.name_input())
            print("Please enter new values...")
            self.activity_add()

    #remove a line
        elif n == "3":
            self.activity_remove(self.name_input())

        else:
            self.main()

    def get_activity_info(self):
        name = input("Name: ")
        description = input("Description: ")
        unit_id = self.unit_type_input()  # unit_type_input is a function that prompts the user to choose a unit and returns the unit ID
        return name, description, unit_id

    def validate_file_activity(self):
        if not os.path.exists(self.activity_csv):
            with open(self.activity_csv, 'w', encoding='UTF8') as f:
                writer = csv.writer(f)
                writer.writerow(self.activity_header)
                f.close()

    def activity_print(self):
        activities = []
        self.validate_file_activity()
        with open(self.activity_csv, encoding='UTF8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                activities.append({"Name": row["name"], "Description": row["description"], "Unit": row["unit"]})
            print(tabulate.tabulate(activities, headers="keys", tablefmt='grid'))

    def activity_add(self, name, description, unit_id):
        while self.name_validate(name):
            name = input("Already exist. Choose another name: ")
        with open(self.activity_csv, 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow([name, description, self.activity_unit[unit_id-1]])
            f.close()

    def activity_remove(self, name):
        with open(self.activity_csv, 'r') as inp, open(self.activity_csv_temp, 'w') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                if row[0] != name:
                    writer.writerow(row)
        with open(self.activity_csv, 'w') as out, open(self.activity_csv_temp, 'r') as inp:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                writer.writerow(row)

    def unit_type_input(self):
        print("Type of unit : ")
        for (i, unit) in enumerate(self.activity_unit, start=1):
            print(i, " - ", unit)
        unit_id = int(input("Input the number: "))
        return unit_id

    def name_validate(self, name):
        with open(self.activity_csv, encoding='UTF8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if name == row["name"]:
                    return True
            return False

    def name_input(self):
        name_input = " "
        while self.name_validate(name_input) is False:
            print("What activity ? ")
            self.activity_print()
            name_input = input("Name: ")
        return name_input

    def entry_print(self):
        entries = []
        self.validate_file_entry()
        with open(self.entry_csv, encoding='UTF8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                entries.append({"Date": row["date"], "Activity": row["activity"], "Quantity": row["qtt"]})
            print(tabulate.tabulate(entries, headers="keys", tablefmt='grid'))

    def entry_input(self):
        entry_name = self.name_input()
        with open(self.activity_csv, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if entry_name == row["name"]:
                    entry_unit = row["unit"]
        entry_qtt = input(f"How many {entry_unit} ?")
        self.validate_file_entry()
        with open(self.entry_csv, 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.datetime.now(), entry_qtt, entry_name])
            f.close()

    def validate_file_entry(self):
        #path = ""
        if exists(self.entry_csv):
            pass
        else:
            print("initializing log...")
            with open(self.entry_csv, 'w', encoding='UTF8') as f:
                writer = csv.writer(f)
                writer.writerow(entry_header)
                f.close()

if __name__ == "__main__":
    tracker = ActivityTracker()
    tracker.main()


"""
Note

ere is an example of how you could integrate SQLite into the ActivityTracker class to replace the use of the CSV file for storing activity data:

Import the sqlite3 module at the top of your script:
Copy code
import sqlite3
In the constructor of the ActivityTracker class, initialize the SQLite database connection and create the activity table if it doesn't exist:
Copy code
def __init__(self):
    self.conn = sqlite3.connect("activity_tracker.db")
    self.cursor = self.conn.cursor()
    self.cursor.execute("""CREATE TABLE IF NOT EXISTS activity (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            description TEXT,
                            unit TEXT)""")
    self.conn.commit()
Replace the validate_file_activity() method with a method that creates an activity table if it doesn't exist.

In the activity_add() method, use the cursor to insert a new activity into the table:

Copy code
def activity_add(self, name, description, unit):
    while self.name_validate(name):
        name = input("Already exist. Choose another name: ")
    self.cursor.execute("""INSERT INTO activity (name, description, unit)
                            VALUES (?, ?, ?)""", (name, description, unit))
    self.conn.commit()
In the activity_remove() method, use the cursor to delete the activity with the specified name:
Copy code
def activity_remove(self, name):
    self.cursor.execute("DELETE FROM activity WHERE name = ?", (name,))
    self.conn.commit()
In the activity_print() method, use the cursor to select all activities from the table and print them:
Copy code
def activity_print(self):
    self.cursor.execute("SELECT * FROM activity")
    activities = self.cursor.fetchall()
    for activity in activities:
        print(activity)


"""
