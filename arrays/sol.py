import ast
import numbers
lstinput = list()
#lstinput = ''
total_inp_value = 0
a = ''
a = list()

while a != "DONE":
    a = input("Enter input Value = ")
    if a.isdigit():
        lstinput.append(a)
        total_inp_value = int(a) + total_inp_value
        print("It's an integer")
    elif '.' in a:
        lstinput.append(a)
        total_inp_value = float(a) + total_inp_value
        print("It's a float")
    elif a != "DONE":
        print("Invalid Input. Please Enter a number")
    continue
print("The input values entered are: ", lstinput)
print("Max number is the list is: ", max(lstinput))
print("Min number is the list is: ", min(lstinput))
# def max_number (lstinputArray):
#     max1 = lstinputArray[0]
#     for i in lstinputArray:
#         if i > max1:
#             max1 = i
#     return max1
# max_number (lstinputArray)
# print("Max value in list is: ", max_number(lstinputArray))
#
# def min_number (lstinputArray):
#     min1 = lstinputArray[0]
#     for i in lstinputArray:
#         if i < min1:
#             min1 = i
#     return min1
# min_number (lstinputArray)
# print("Min value in list is: ", min_number(lstinputArray))
print("Total value of all user input is : ", total_inp_value)

def Average(lstinput):
    len_lstinputArray = len(lstinput)
    avg_lstinputArray1 = total_inp_value / len_lstinputArray
    avg_lstinputArray = float(avg_lstinputArray1)
    return avg_lstinputArray

average = Average(lstinput)
print("Average of the list is: ", average)

print ("============ Date Program ================")
date_entry = input('Enter a date in YYYY-MM-DD format:  ')
datstr = date_entry.split("-")
if datstr[1] == '01':
    print("Output Month is January of", datstr[0])
elif datstr[1] == '02':
    print("Output Month is February", datstr[0])
elif datstr[1] == '03':
    print("Output Month is March", datstr[0])
elif datstr[1] == '04':
    print("Output Month is April", datstr[0])
elif datstr[1] == '05':
    print("Output Month is May", datstr[0])
elif datstr[1] == '06':
    print("Output Month is June", datstr[0])
elif datstr[1] == '07':
    print("Output Month is July", datstr[0])
elif datstr[1] == '08':
    print("Output Month is August", datstr[0])
elif datstr[1] == '09':
    print("Output Month is September", datstr[0])
elif datstr[1] == '10':
    print("Output Month is October", datstr[0])
elif datstr[1] == '11':
    print("Output Month is November", datstr[0])
elif datstr[1] == '12':
    print("Output Month is December", datstr[0])