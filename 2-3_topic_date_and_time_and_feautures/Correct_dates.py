'''
Write a program that takes a sequence of dates as input and checks each of them for correctness.

Input format
The input to the program is a sequence of dates in the format DD.MM.YYYY, each on a separate line.
The end of the sequence is the word end.

Output format
For each date entered, the program should display the text Correct or Incorrect, depending on whether
the date is correct, and then display the number of correct dates.
'''

from datetime import date
count= 0
while True:
    k = input()
    if k == "end":
        print(count)
        break
    day, month, year = [int(i) for i in k.split(".")]
    try:
        myd = date(year, month, day)
        print("Correct")
        count+=1
    except:
        print("Incorrect")

# Input:
# 19.05.2016
# 05.13.2010
# 21.12.2012
# 01.01.1000
# 32.04.2003
# end
# Output:
# Correct
# Incorrect
# Correct
# Correct
# Incorrect
# 3