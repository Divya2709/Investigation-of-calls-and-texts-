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
Forming the seperate list of those people who call to other in calls list and convert it into the set

"""

list1 = [ ]
for i in range(0,len(calls)):
    list1.append(calls[i][0])
    set1 = set(list1)

"""
Forming the seperate list of those people who receive the call in calls list and convert it into the set

"""

list2 = [ ]
for j in range(0,len(calls)):
    list2.append(calls[j][1])
    set2 = set(list2)


"""
Forming the seperate list of those people who texts to other in texts list and convert it into the set

"""

list3 = [ ]
for k in range(0,len(texts)):
    list3.append(texts[k][0])
    set3 = set(list3)



"""
Forming the seperate list of those people who received the texts from other in texts list and convert it into the set

"""
list4 = [ ]
for l in range(0,len(texts)):
    list4.append(texts[l][1])
    set4 = set(list4)


"""
Combine the all Number in one varible with no duplication

"""
count_set =  (set1 | set2 | set3 | set4)


#Print the length of combine variable
print(f"There are {len(count_set)} different telephone numbers in the records.")


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
