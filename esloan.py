print(25 > 10)
userinput = input('Do you already have a mortgage?: y for yes and n for no: ' )
if (userinput == 'y'):
    print("you cannot take another mortgage")
elif (userinput == 'n'):
    propertyvalue = int(input('What is the value of the property: '))
    min20percent = propertyvalue * 0.2
    print(min20percent)
    annualsalary = int(input('what is your annual salary: '))
    if (min20percent < annualsalary):
        upfront10percent =int(propertyvalue * 0.1)
        print(upfront10percent)
        upfront = int(input('How much is your upfront payment?: '))
        if upfront > upfront10percent:
            monthly25percent = annualsalary * 0.25
            monthlyspending = int(input('What is your monthly spendings'))
            if monthlyspending < monthly25percent:
                print('You can take a mortgage')
            else:
                print('You cannot take a mortgage')
        else:
            print('You are not viable to take a mortgage')
    else:
        print('You are not viable for another mortgage')