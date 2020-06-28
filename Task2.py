"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
Creating the empty dictionary for storing the compare numbers and compare each numbers for finding the longest duration call along with the seconds

"""
dict_num = {}
telephone_num = 0
longest_time = 0
for numbers in calls :
    dict_num[numbers[0]] = dict_num.get(numbers[0],0) + int(numbers[-1])
    dict_num[numbers[1]] = dict_num.get(numbers[1],0) + int(numbers[-1])
    if dict_num[numbers[0]] > longest_time:
        telephone_num = numbers[0]
        longest_time = dict_num[numbers[0]]
    if dict_num[numbers[1]] > longest_time:
        telephone_num = numbers[1]
        longest_time = dict_num[numbers[1]]

print(f"{telephone_num} spent the longest time,seconds,{longest_time} on the phone during September 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
