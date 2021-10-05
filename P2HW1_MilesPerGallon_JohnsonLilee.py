#This program will calculates miles per gallon, total gas cost, and
#cost per mile.
#05 Oct. 2021
#CTI-110 P2HW1-Miles Per Gallon
#Lilee Johnson
#-------------------------------------------------------------------------
#pesudocode
#prompt user for mileDrive
#prompt user for galUse
#prompt user for costPerGal
#milePerGal = mileDrive / galUse
#totalCost = costPerGal * galUse
#costPerMile = milePerGal / totalCost
#display Miles Per Gallon, Total Gas Cost, Cost Per Mile
#-------------------------------------------------------------------------
mileDrive = float(input("Enter miles driven > "))
galUse = float(input("Enter gallons used > "))
costPerGal = float(input("Enter cost per gallon > "))
milePerGal = mileDrive / galUse
totalCost = costPerGal * galUse
costPerMile = milePerGal / totalCost
print('Miles Per Gallon:  {:.2f}'
      '\nTotal Gas Cost:   ${:.2f}'
      '\nCost Per Mile:    ${:.2f}'.format(milePerGal, totalCost, costPerMile))
