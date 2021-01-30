#Jackson Eubank
#CS362
#HW3

#input
leapYear = 0;
year = input("Enter a year (int): ");

while not (year.isdigit()):
    print("Oops! Looks like you didn't enter an integer! Try again.\n");
    year = input("Enter a year (int): ");

year = int(year);

#leap year calculation
if (year % 4 == 0):
    leapYear = 1;
    if (year % 100 == 0 and year % 400 != 0):
        leapYear = 0;
else:
    leapYear = 0;

#output
if (leapYear):
    print(year, "is a leap year.");
else:
    print(year, "is NOT a leap year.");

#program end
input("\nPress [ENTER] to exit the program...");
