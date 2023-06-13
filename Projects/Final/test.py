import csv


def name_validate(inp):
    with open('/home/max/Documents/Code/EDX/Final/activity.csv', encoding='UTF8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if inp == row["name"]:
                return True
        return False

print(name_validate("d"))
