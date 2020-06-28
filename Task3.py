"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
"""
Creating the empty list to store the data of:
list_code = to store the data of receiver code
list_080 = to store the number which starts with 080
list1_080 = to store the number who received the 080 codes calls



Convert the list into set and again list or calculate the length of list_080

"""

list_code = []
list_080 = []
list1_080= []
print("The numbers called by people in Bangalore have codes:")
for i in range(0,len(calls)):
    if calls[i][0][0] == "(" and calls[i][0][1] == "0" and calls[i][0][2] == "8" and calls[i][0][3] == "0" and calls[i][0][4] == ")":
        list_code.append(calls[i][1][0:5])
        list_080.append(calls[i][0])
        list1_080.append(calls[i][1])
set_code = sorted(list(set(list_code)))
total_080 = len(set(list_080))

"""
Print the code in seperate line

"""
for k in range(0,len(set_code)):
    print(set_code[k])

"""
Extract the received number whose code is 080 and calculate length

"""
list2_080 = []
for j in range(0,len(list1_080)):
    if calls[j][1][0] == "(" and calls[j][1][1] == "0" and calls[j][1][2] == "8" and calls[j][1][3] == "0" and calls[j][1][4] == ")":
        list2_080.append(calls[j][1])
received_080 = len(set(list2_080))


"""
Calculating the percentage of people in bangalore who called the people in bangalore

"""


percentage = (received_080/total_080)*100
print(f"{round(percentage,2)} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")




"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
