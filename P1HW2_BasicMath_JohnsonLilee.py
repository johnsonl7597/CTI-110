#This is a program that allows the user to enter the name and cost of expense.
#Then it will calculate 6% tax and tell the user how much they will be spending.
#(for each month and year)
#28 Sept. 2021
#CTI-110, P1HW2-Basic Math
#Lilee Johnson
#------------------------------------------------------------------------------
#PSEUDOCODE
#promt user for ExpenNam
#promt user for ChargMonth
#ChargMonth * .06 = MonthTax
#MonthTotal = ChargMonth + MonthTax
#MonthTax * 12 = YearTax
#display results
#------------------------------------------------------------------------------
expenNam = input('Enter name of expense > ')
chargMonth = int(input('Enter monthly charge > '))
monthTax = chargMonth * .06
monthTotal = chargMonth + monthTax
yearTax = monthTotal * 12
print(
    """\nBill: {EN} ----Before Tax: ${CM:.2f}
    Monthly Tax:    ${MT:.2f}
    Monthly Charge: ${MonthT:.2f}
    Annual Charge:  ${YT:.2f}""".format(EN = expenNam,
                                        CM = chargMonth,
                                        MT = monthTax,
                                        MonthT = monthTotal,
                                        YT = yearTax))
