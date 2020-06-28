Task0
print(f"First record of texts, {texts[0][0]} texts {texts[0][1]} at time {texts[0][2]}")                               -----constant time
print(f"Last record of calls, {calls[-1][0]} calls  at time {calls[-1][1]}, lasting {calls[-1][2]} seconds")           -----constant time

It contains only two print statement that's why it takes the constant time to run the code. Beacause simple statements takes constant time (in milliseconds) to run the program.
So, The time complexity for the task0 is 0(1).




Task1
It contains the four consecutive for loop an many more constants statements.

list1 = [ ]                                                               ---- constant  time (c11)
for i in range(0,len(calls)):                                             ---- n time
    list1.append(calls[i][0])                                             ---- constant  * n time(c1*n)
    set1 = set(list1)                                                     ---- constant * n time(c2*n)

list2 = [ ]                                                               ---- constant time(c12)
for j in range(0,len(calls)):                                             ---- n time
    list2.append(calls[j][1])                                             ---- constant * n time(c3*n)
        set2 = set(list2)                                                 ---- constant * n time(c4*n)

list3 = [ ]                                                               ---- constant time(c13)
    for k in range(0,len(texts)):                                         ---- n time
        list3.append(texts[k][0])                                         ---- constant * n time(c5*n)
        set3 = set(list3)                                                 ---- constant * n time(c6*n)

list4 = [ ]                                                               ---- constant time(c14)
    for l in range(0,len(texts)):                                         ---- n time
        list4.append(texts[l][1])                                         ---- constant * n time(c7*n)
        set4 = set(list4)                                                 ---- constant * n time(c8*n)


count_set =  (set1 | set2 | set3 | set4)                                  ---- constant time(c15)
print(f " There are {len(count_set)} different telephone numbers in the records.")----constant time(c16)

The run time analysis of the program is :
= c11 + (c1*n + c2*n) + c12 +(c3*n + c4*n) + c13 + (c5*n + c6*n) + c14 + (c7*n + c8*n)
= c11 + n(c1+ c2) + c12 + n(c3 + c4) + c13 + n(c5 + c6) + c14 + n(c7 + c8)
= c11 + n(c) + c12 + n(c") + c13 + n(c"') + c14 + n(c"")

after removing all constants .The program will take the n time to run the program.
So the time complexity is 0(n) for task1.




Task2
It contains the following code :


dict_num = {}                                                                                                                               -----constant time (c1)
telephone_num = 0                                                                                                                           -----constant time(c2)
longest_time = 0                                                                                                                            -----constant time(c3)
for numbers in calls :                                                                                                                      -----n time
    dict_num[numbers[0]] = dict_num.get(numbers[0],0) + int(numbers[-1])                                                                    -----constant * n time(c4*n)
    dict_num[numbers[1]] = dict_num.get(numbers[1],0) + int(numbers[-1])                                                                    -----constant * n time(c5*n)
    if dict_num[numbers[0]] > longest_time:                                                                                                 -----constant * n time(c6*n)
        telephone_num = numbers[0]                                                                                                          -----constant * n time(c7*n)
        longest_time = dict_num[numbers[0]]                                                                                                 -----constant * n time(c8*n)
    if dict_num[numbers[1]] > longest_time:                                                                                                 -----constant * n time(c9*n)
        telephone_num = numbers[1]                                                                                                          -----constant * n time(c10*n)
        longest_time = dict_num[numbers[1]]                                                                                                 -----constant * n time(c11*n)

print(f"{telephone_num} spent the longest time,seconds,{longest_time} on the phone during September 2016.")                                 -----constant time(c12)
= c1 + c2 + c3 + (c4*n + c5 *n + c6*n + c7*n + c8*n +c9*n + c10*n + c11*n) + c12
= n(c4 + c5 + c6 + c7 + c8 + c9 + c10 + c11)
= n(c)
After removing all constants the program will takes the n time to run the code.
The time complexity of task2 is 0(n).

Task3
It contains the following code :

list_code = []                                                                                                                                               ----constant time(c1)
list_080 = []                                                                                                                                                ----constant time(c2)
list1_080= []                                                                                                                                                ----constant time(c3)
print("The numbers called by people in Bangalore have codes:")                                                                                               ----constant time(c4)
for i in range(0,len(calls)):                                                                                                                                ----n time
    if calls[i][0][0] == "(" and calls[i][0][1] == "0" and calls[i][0][2] == "8" and calls[i][0][3] == "0" and calls[i][0][4] == ")":                        ----constant * n time(c5*n)
        list_code.append(calls[i][1][0:5])                                                                                                                   ----constant * n time(c6*n)
        list_080.append(calls[i][0])                                                                                                                         ----constant * n time(c7*n)
        list1_080.append(calls[i][1])                                                                                                                        ----constant * n time(c8*n)

set_code = sorted(list(set(list_code)))                                                                                                                      ----constant time(c9)
total_080 = len(set(list_080))                                                                                                                               ----constant time(c10)

for k in range(0,len(set_code)):                                                                                                                             ----n time
    print(set_code[k])                                                                                                                                       ----constant * n time(c11*n)

list2_080 = []                                                                                                                                               ----constant time(c12)
for j in range(0,len(list1_080)):                                                                                                                            ----n time
    if calls[j][1][0] == "(" and calls[j][1][1] == "0" and calls[j][1][2] == "8" and calls[j][1][3] == "0" and calls[j][1][4] == ")":                        ----constant * n time(c13*n)
        list2_080.append(calls[j][1])                                                                                                                        ----constant * n time(c14*n)
        received_080 = len(set(list2_080))                                                                                                                   ----constant * n time(c15*n)

percentage = (received_080/total_080)*100                                                                                                                    ----constant time(c16)
print(f"{round(percentage,2)} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")                                  ----constant time(c17)

The run time analysis of this task is :
= c1 + c2 + c3 + ( c5*n+c6*n+c7*n+c8*n) + c9 + c10 + c11*n + c12 + (c13*n + c14*n + c15*n) + c16 + c17
ignore all constants
= n(c5 * c6 * c7 * c8) + c11*n +(n(c13 + c14 + c15))
= n + c11*n + n
= 2n + c11*n
ignore all constants
= n
The time complexity of task3 is 0(n).




Task4
It contains the following code :

list1 = [ ]                                                               ---- constant  time (c11)
for i in range(0,len(calls)):                                             ---- n time
    list1.append(calls[i][0])                                             ---- constant  * n time(c1*n)
    set1 = set(list1)                                                     ---- constant * n time(c2*n)

list2 = [ ]                                                               ---- constant time(c12)
for j in range(0,len(calls)):                                             ---- n time
    list2.append(calls[j][1])                                             ---- constant * n time(c3*n)
        set2 = set(list2)                                                 ---- constant * n time(c4*n)

list3 = [ ]                                                               ---- constant time(c13)
    for k in range(0,len(texts)):                                         ---- n time
        list3.append(texts[k][0])                                         ---- constant * n time(c5*n)
        set3 = set(list3)                                                 ---- constant * n time(c6*n)

list4 = [ ]                                                               ---- constant time(c14)
    for l in range(0,len(texts)):                                         ---- n time
        list4.append(texts[l][1])                                         ---- constant * n time(c7*n)
        set4 = set(list4)                                                 ---- constant * n time(c8*n)


count_set =  (set1 - (set2 | set3 | set4))                                ----constant time(c15)
convert_list = list(count_set)                                            ----constant time(c16)
sorted1 = sorted(convert_list)                                            ----constant time(c17)

print(f"These numbers could be telemarketers: ")                          ----constant time(c18)
for m in range(0,len(sorted1)) :                                          ----n time
    if sorted1[m][0] == "1":                                              ----constant * n time(c19*n)
        print(sorted1[m])                                                 ----constant * n time(c20*n)

The run time analysis of the program is :
        = c11 + (c1*n + c2*n) + c12 +(c3*n + c4*n) + c13 + (c5*n + c6*n) + c14 + (c7*n + c8*n) + c15 + c16 + c17 + c18 + (c19*n + c20*n)
        = c11 + n(c1+ c2) + c12 + n(c3 + c4) + c13 + n(c5 + c6) + c14 + n(c7 + c8) + c15 + c16 + c17 + c18 + n(c19 + c20)
        = c11 + n(c) + c12 + n(c") + c13 + n(c"') + c14 + n(c"") + c15 + c16 + c17 + c18 +n(cc""')

after removing all constants .The program will take the n time to run the program.
So the time complexity is 0(n) for task4.
