# Application "Count me One"
## By Max
## 2022-12-22
## Montreal, Canada

### Video Demo: https://lekingfu.com/nextcloud/s/FfxRRdxb6zf3rR9
#### Roadmap:

1. MVP <-- You are here!
2. GUI
3. Rewards
4. Data analytics
5. Packaged as a mobile app

#### Description:

This simple application is useful to keep track of anything and everything.
Since the application is still in its infancy, all the code is still in a single file, "project.py".
It also uses 2 csv files that explained later.
The main concept are "Activity" and "Entry".

The former allows you to keep track of your differents activities.
It has the following information : name, description and units.
The application allows you to maintain these activities by allowing :
- Creation of a new activity
- Editing an existing activity
- Removal of an existing activiy
The information is saved in a csv file named "activity.csv".
If it doesn't exist, the application make sure to create it before.
The list of activity is easy to consult with the "Show activites" function.

As for the entry, it allows to enter the monitoring of an activity.
This function allows you to choose an existing activity and input the corresponding quantity.
All entries are available with the "Show entries" function.
The information is saved in a csv file named "log.csv".
Like the previous file, the application make sure the file exist and if it doesn't, it will create before you need it.

In most function, there are controls to make sure the value selected exist.
If it doesn't exist, a new prompt is showed.

You can input an "X" to either go to the previous menu or to quit the application.
