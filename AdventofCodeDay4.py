## Advent of Code Day 4
'''
The Elf leads you over to the pile of colorful cards. There, you discover dozens of scratchcards, all with their opaque covering already scratched off. 
Picking one up, it looks like each card has two lists of numbers separated by a vertical bar (|): a list of winning numbers and then a list of numbers you have. 
You organize the information into a table (your puzzle input).

As far as the Elf has been able to figure out, you have to figure out which of the numbers you have appear in the list of winning numbers. The first match makes the card worth one point
 and each match after the first doubles the point value of that card.

Sample Card -              Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53

Take a seat in the large pile of colorful cards. How many points are they worth in total?
'''
## Opening file without error handling, sorry!
fname = 'advent4.txt'
fhand = open(fname)

## Creating dictionary to store card # and resultant winnings by card
result_dict = dict()

## Going through each line to separate out the winning numbers and our numbers and then comparing them
for line in fhand:
    line = line.strip()
    winning_nums = line[line.find(":")+1:line.find("|")]
    winning_list = winning_nums.strip().split()
    our_nums = line[line.find("|")+1:]
    our_list = our_nums.strip().split()

    win_counter = 0
    winning_nums = []

    for num in winning_list:
        if num in our_list:
            winning_nums.append(num)
            win_counter += 1
    
    # Calculating the winning $ amount for each card
    card_winnings = 0
    if win_counter == 1 or win_counter == 2:
        card_winnings = win_counter
    elif win_counter > 2:
        card_winnings = 2**(win_counter-1)
    elif win_counter == 0:
        card_winnings = 0
    else:
        print("Error calculating your winnings I am sooooo sorry!")

    # Saving the card number and winnings amount to our results dictionary
    card_num = line[line.find(" "):line.find(":")].strip()
    result_dict[card_num] = card_winnings

## Totalling up the winnings and then printing it out
total_winnings = 0
for value in result_dict.values():
    total_winnings += value
print("OK there hombre, your elf friend has won a total of $%s" % total_winnings)