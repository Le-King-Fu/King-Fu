import project
import csv
import os

absolute_path = os.path.dirname(__file__)
activity_csv = str(absolute_path + "/activity.csv")

#activities = [{'name':'play', 'description':'video game', 'unit':'hours'},
#{'name':'meditation', 'description':'dont think', 'unit':'minutes'}]

#def name_validate(inp):
#    with open('/home/max/Documents/Code/EDX/Final/test_activity.csv', encoding='UTF8') as f:
#        reader = csv.DictReader(f)
#        for row in reader:
#            if inp == row["name"]:
#                return True
#        return False

def test_name_validate():
    assert project.name_validate("") == False
    assert project.name_validate("patato") == False
    assert project.name_validate("play") == True
    #assert project.name_validate("test") == True
#    assert project.name_validate("play") == False

def test_activity_add():

    # Count the record pre-test
    with open(activity_csv, 'r', encoding='UTF8') as f:
        reader = csv.DictReader(f)
        activities = [row for row in reader]
    nb_item_start = len(activities)

    # Call the activity_add function with a new activity
    project.activity_add("Test Activity","This is a test activity",2)

    # Count the record post-test
    with open(activity_csv, 'r', encoding='UTF8') as f:
        reader = csv.DictReader(f)
        activities = [row for row in reader]
    nb_item_end = len(activities)

    #assert nb_item_end == int(nb_item_start + 1)  # there should now be n+1 activities in the file
    assert activities[-1]['name'] == "Test Activity"  # the last activity should be the new one
    assert activities[-1]['description'] == "This is a test activity"
    assert activities[-1]['unit'] == "units"

    #clean-up post-test
    project.activity_remove("Test Activity")

def test_activity_remove_nonexistent():

    # Check that the activity_csv file has not been modified
    with open(activity_csv, 'r', encoding='UTF8') as f:
        reader = csv.DictReader(f)
        activities = [row for row in reader]
    nb_item = len(activities)

    # Call the activity_remove function with a non-existent activity
    project.activity_remove("Non-Existent Activity")

    assert len(activities) == nb_item  # there should still be n activities in the file
