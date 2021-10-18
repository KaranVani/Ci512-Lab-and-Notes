userinput = input('Do you already have a mortgage?: y for yes and n for no: ' )
if (userinput == 'y'):
    print("you cannot take another mortgage")
elif (userinput == 'n'):
    propertyvalue = input('What is the value of the property: ')
    minannualsalary = propertyvalue * 0.2
    annualsalary = input('what is your annual salary: ')
    if (annualsalary < minannualsalary):
        print('You broke')