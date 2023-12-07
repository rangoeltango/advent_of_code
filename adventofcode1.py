'''Advent of Code Day 1
--- Day 1: Trebuchet?! ---
The calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills.
Consequently, the Elves are having trouble reading the values on the document. 
The calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. 
On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
For example:     1abc2       pqr3stu8vwx       a1b2c3d4e5f          treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
ANSWER - >> Consider your entire calibration document. What is the sum of all of the calibration values?'''

## Importing Regular Expressions
import re

## Hard coding file name, but providing error below in case there is issue finding it
fname = 'advent1.txt'
try:
    fhand = open(fname)
except:
    print("File could not be opened. Please check the directory location and filename then try again!")

## Creating list to store calibration values & sum to total them
#cal_vals = list() ### optional to create a list of cal_vals
sum = 0

## Going through each line in the file
for line in fhand:
    nums_in_line = re.findall('[0-9]+',line)
    cal_val_current = (nums_in_line[0][0])+(nums_in_line[-1][-1])
    #cal_vals.append(cal_val_current) ### optional to add to list of cal_vals
    sum += int(cal_val_current)

## Printing out answers (list of cal vals optional)
#print(cal_vals) ### optional to print out all cal_vals
print("\nThe sum of all calibration values is %s.\n" % sum)
