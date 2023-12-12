'''Advent of Code Day 2 - 
--- Day 2: Cube Conundrum! ---
As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, 
and your goal is to figure out information about the number of cubes. To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes,
show them to you, and then put them back in the bag. He'll do this a few times per game. You play several games and record the information from each game (your puzzle input). Each game is listed
 with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red;              1 red, 2 green, 6 blue;       2 green
Game 2: 1 blue, 2 green;            3 green, 4 blue, 1 red;       1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red;    5 blue, 4 red, 13 green;      5 green, 1 red
Game 4: 1 green, 3 red, 6 blue;     3 green, 6 red;               3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green;     2 blue, 1 red, 2 green

In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes;
the third set is only 2 green cubes. The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed
 you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

##Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?'''

## Opening file without error checking, sorry! I named my dataset advent2.txt as you can see!
fname = 'advent2.txt'
fhand = open(fname)

## Establishing maximum cube count conditions from prompt
max_red, max_green, max_blue = 12, 13, 14

## Establishing dictionaries to hold all games and then the different possible & impossible game sets
games_dict = dict()
possible_games = dict()
impossible_games = dict()

## Finding first the game numbers, then the game results and saving them in games_dict
for game in fhand:
    colon_ind = game.index(":")
    space_ind = game.index(" ")
    game_num = game[space_ind+1:colon_ind]

    # Finding & saving the game results
    game_trim = game[colon_ind+1:]
    game_trimmed = game_trim.strip()
    game_turns = game_trimmed.split(";")
    games_dict[game_num] = game_turns

## Going through each game in the dictionary and walking through each set of 'reveals' to find the max observations of each color
for game in games_dict:
    game_max_record = {"red" : 0, "green" : 0, "blue" : 0}
    
    # For each sub-part of a game - a 'reveal' of the hand for example, looking at the cube colors and comparing them to the game-level max cubes
    for reveal in games_dict[game]:
        reveal_cubes = reveal.split(",")
        for cube in reveal_cubes:
            cube = cube.strip()
            cube_color = cube[cube.find(' '):].strip()
            cube_num = int(cube[:cube.find(' ')].strip())

            # If this cube number is higher than the highest seen this game, it becomes the new high observation
            if cube_num > game_max_record[cube_color]:
                game_max_record[cube_color] = cube_num

    # Checking if all cubes are possible, and if so saving this record to the possible games, else to the impossible games
    if (game_max_record["red"] <= max_red) and (game_max_record["green"] <= max_green) and (game_max_record["blue"] <= max_blue):
        possible_games[game] = games_dict[game]
    else:
        impossible_games[game] =  games_dict[game]

## Results printing
print("\nAfter looking through all of the games in the 'games_dict' dictionary, I sorted the possible and impossible games for you.")
print("We saved them to the dictionaries 'possible_games' and 'impossible_games' in case you want to take a look.\n")

## Listing the possible games and then their total
possible_key_sum = 0
for key in possible_games.keys():
    possible_key_sum += int(key)
print("The possible games total:", possible_key_sum)

## Listing the impossible games and then their total
impossible_key_sum = 0
for key in impossible_games.keys():
    impossible_key_sum += int(key)
print("The impossible games total:", impossible_key_sum)
