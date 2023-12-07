## Importing Regular Expressions
import re
fname = 'advent1.txt'
fhand = open(fname)

## Creating a function to convert any 'number words' to their integer values
def words_to_num(wordstring):
    word_num_list = {'one':'1','two':'2','three':'3','four':'4','five':'5', 'six':'6', 'seven':'7', 'eight':'8','nine':'9'}
    pattern = re.compile(r'('+'|'.join(word_num_list.keys())+r')')
    return re.sub(pattern, lambda x: word_num_list[x.group()], wordstring)

## Creating sum to store total
sum = 0

## Going through each line in the file
for line in fhand:
    modded_line = words_to_num(line)
    nums_in_line = re.findall('[0-9]+', modded_line)
    cal_val_current = (nums_in_line[0][0])+(nums_in_line[-1][-1])
    sum += int(cal_val_current)

## Printing out answers (list of cal vals optional)
print("\nThe sum of all calibration values is %s.\n" % sum)
