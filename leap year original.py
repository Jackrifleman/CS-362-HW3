#Jackson Eubank
#CS362
#HW1

#input
year = int(input("Enter a year (int): "));
leapYear = 0;

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
input("\nPress any key to continue...");
