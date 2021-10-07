#This program will demonstrate the students understanding of lists and sets.
#CTI-110, P2HW2 - List and Sets
#Lilee Johnson
#05 Oct 2021
#-----------------------------------------------------------------------------
#pesudocode
#prompt user for 6 indivual numbers
#store the numbers in a list called List6
#display lowNum, highNum, total, average
#set(List6)
#display List6, set
#-----------------------------------------------------------------------------
num1 = int(input("Enter number 1 of 6 > "))
num2 = int(input("Enter number 2 of 6 > "))
num3 = int(input("Enter number 3 of 6 > "))
num4 = int(input("Enter number 4 of 6 > "))
num5 = int(input("Enter number 5 of 6 > "))
num6 = int(input("Enter number 6 of 6 > "))
list6 = [num1, num2, num3, num4, num5, num6]
print("\nList6 list:\n", list6)
lowNum = min(list6)
highNum = max(list6)
total = num1 + num2 + num3 + num4 + num5 + num6
average = total / 6
listSix = {num1, num2, num3, num4, num5, num6}
print("smallest number in List6: ", lowNum)
print("LARGEST number in List6:  ", highNum)
print("Sum of numbers in List6:  ", total)
print("The average in List6:     ", average)
print("\nListSix set:\n", listSix)
