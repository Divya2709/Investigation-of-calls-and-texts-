# Investigation-of-calls-and-texts-
In this project, There are five task on the Investigating Texts and Calls. On the basis of given instruction,we have to investigate the data of texts and calls. 
The text and call data are provided in csv files.
The text data (text.csv) has the following columns: 
1]Column0: Sending telephone number(String) 
2]Column1: Receiving telephone number(String)
3]Column2: Timestamp of text message(String)
The call data (call.csv) has the following columns: 
1]Column0: Calling telephone number(String) 
2]Column1: Receiving telephone number(String)
3]Column2: Start timestamp of telephone call(String)
3]Column3: Duration of telephone call in seconds(String)
All telephone numbers are 10 or 11 numerical digits long. Each telephone number starts with a code indicating the location and/or type of the telephone number.
There are three different kinds of telephone numbers, each with a different format:
1)Fixed lines start with an area code enclosed in brackets. The area codes vary in length but always begin with 0. Example: "(022) xxxxxxxx" , "(080) xxxxxxxx" and many more fixed line code.
2)Mobile numbers have no parentheses, but have a space in the middle of the number to help readability. The mobile code of a mobile number  its first four digits and they always start with 7, 8 or 9. Example: "93412 66159".
3)Telemarketers's numbers have no parentheses or space, but start with the code 140. Example: "140xxxxxxx".
