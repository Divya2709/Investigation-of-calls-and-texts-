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
Finding those number which present in only calling list but not present into the receiving call ,sending text as well as receiving text and convert it into the list and sort them

"""
count_set =  (set1 - (set2 | set3 | set4))
convert_list = list(count_set)
sorted1 = sorted(convert_list)

"""
Printing only those number which starts with 140

"""
print(f"These numbers could be telemarketers: ")
for m in range(0,len(sorted1)) :
    if sorted1[m][0] == "1":
        print(sorted1[m])


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
