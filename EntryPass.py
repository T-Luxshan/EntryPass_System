# Getting input from user.
def getInput():
    space = " "
    print("_" * 50)
    print(space * 10 + "Welcome to DSIT seminar")
    name = input("Name of Participant" + space * 24 + ":")
    place = input("Place" + space * 38 + ":")
    category = input("Category (S)tudent/(E)mployee/(U)nEmployee :")
    print("_" * 50)
    return name, place, category


# Printing the Data
def printEntry(no, name, place, category):
    print("                 Data Science In Tamil")
    print("                    Jaffna, Srilanka")
    print("                    on Data Science")
    print("                   E N T R Y P A S S")
    print("Pass No:", no)
    print("Name    :", name)
    print("Place   :", place)
    print("Category:", category)


# Initiate the Variables.
participant = 99
student = 58
employee = 23
un_employee = 17
participant_category = ['s', 'e', 'u', 'student', 'employee', 'unemployee']  # Category types.

while participant <= 100:
    entry = getInput()
    third_entry = entry[2].lower()
    if third_entry in participant_category:  # Check the category.
        if third_entry == 'student' or third_entry == 's':
            student += 1
            cate = 'Student'
        elif third_entry == 'employee' or third_entry == 'e':
            employee += 1
            cate = "Employee"
        else:
            un_employee += 1
            cate = 'Un_Employee'
        printEntry(participant, entry[0], entry[1], cate)
        participant += 1

    else:
        print("Invalid Category")
print()
print("HOUSEFUL")
print()
report = input("Do you want Report <Y/N> :")  # Ask for report.

if report.lower() == 'y':
    print("_" * 50)
    print("                 Data Science In Tamil")
    print("                    Jaffna, Srilanka")
    print("                    on Data Science")
    print("                      R E P O R T")
    print("No.of.Students:", student)
    print("No.of.Employees:", employee)
    print("No.of.Un Employees:", un_employee)
    print("_" * 50)
