# This program will calculate employee pay according to input from the user.
# Mr. Teter, P3HW2 - Salary
# Lilee Johnson
# 29 Oct 2021
#--------------------------PESUDOCODE-----------------------------
# Asks the user for employee, empHours, PayRate
# Evaluate if employee has worked overtime. If yes calcuate amount owed to
#employee for overtime hours
# Calculate amount employee shoud be paid for regular hours worked.
# Display grossPay, employee, PayRate,ArithmeticError empHours,
#overHr, overPay, pay
def main():
    employee = input("Enter employee name > ")
    empHours = float(input("Enter number of hours they worked this month > "))
    payRate = float(input("Enter pay rate > "))
    if input("Enter 'yes' or 'no' for if employee worked overtime > ") == "yes":
        overHr = float(input("Enter amount of overtime > "))
        overPay = overHr * payRate * 1.5
        pay = empHours * payRate
        grossPay = overPay + pay
        print("\nEmployee name:      ", employee)
        print("\nHours Worked     Pay Rate     OverTime ",
              "OverTime Pay")
        print("--------------------------------",
              "--------------------------------")
        print("     ", '{:.2f}'.format(empHours), "     ",
              '{:.2f}'.format(payRate), "        ",
              overHr, "     ", '{:.2f}'.format(overPay))
        print("Regular Hour Pay     Gross Pay\n",
              "---------------------------------------")
        print("     ", '{:.2f}'.format(pay), "          ",
              '{:.2f}'.format(grossPay))
    else:
        pay = empHours * payRate
        print("\nEmployee name:      ", employee)
        print("\nHours Worked     Pay Rate",
              "     Regular Hour Pay     Gross Pay")
        print("---------------------------------",
              "---------------------------------")
        print("     ", '{:.2f}'.format(empHours)
              , "        ", '{:.2f}'.format(payRate),"        ",
              '{:.2f}'.format(pay), "           ", '{:.2f}'.format(pay))
main()
