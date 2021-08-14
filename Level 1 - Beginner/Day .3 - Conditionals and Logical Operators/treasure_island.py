"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 3
PROJECT: TREASURE ISLAND
LEVEL: BEGINNER

INSTRUCTIONS:

    1. Create a storyline for your treasure hunt adventure
    2. Using if loops, ask for users to make choices for the story along the way
    3. With each choice, the user will progress until they find the treasure, or choose wrong

"""

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.') 

gameOver = '''
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
'''

print(
    '\n',
    100 * '~' + '\n',
    '\n',
    'You and your crew have crashed onto the shores of an island in the Carribbean sea.' + '\n',
    'The island was not on any known map, and your GPS can\'t locate you.' + '\n',
    '\n',
    'You find a bottle with a map inside clearly marked with a large "X".' + '\n',
    'The crew cheers! There is a treasure on the island.' + '\n',
    '\n',
    'The map starts nearby along a path that leads from the beach and into the forests.' + '\n', 
    'Just in case someone sails or flies by, you leave some of the crew behind and set off.' + '\n',
    '\n',
    100 * '~' + '\n'
)

print(
    '\n',
    100 * '?' + '\n',
    '\n',
    'Your group enters the path and follows it until you reach a fork in the road.' + '\n',
    'The map does not show you which way to go and the group is split, some want to go left, some want to go right.' + '\n',
    '\n',
    'Which way will you choose, Left or Right?' + '\n',
    '\n',
    100 * '?' + '\n'
)

# Choice 1

choice = input('Enter L for Left or R for Right: ').lower()

if choice != 'l' and choice != 'r':
    print('\n\nSorry, you did not choose correctly.\nA sinkhole swallows your group.')
    print(gameOver)
    exit
elif choice == 'l':
    print('You choose to go left...')
elif choice == 'r':
    print('\n\nSorry, you did not choose correctly.\nAn angry horde of killer bees eat your group.')
    print(gameOver)
    exit

print(
    '\n',
    100 * '~' + '\n',
    '\n',
    'You choose to go left and wander up the mountain path.' + '\n',
    'After what seems like hours, you end up at a stone archway.' + '\n',
    '\n',
    'It appears to enter into the mountain and you can see light coming from inside.' + '\n',
    'You and your group walk into the archway and through the tunnel.' + '\n',
    '\n',
    'Once you reach the other side, the sun hits you through the top of the mountain peak.' + '\n',
    'Around you, there is meadow as far as you can see and a giant lake.' + '\n',
    '\n',
    100 * '~' + '\n'
)

print(
    '\n',
    100 * '?' + '\n',
    '\n',
    'You see a small island in the center with a castle on top just like on the map.' + '\n',
    'There doesn\'t appear to be a way to get across the lake.' + '\n',
    '\n',
    'What will you do, stop and rest or will you swim?' + '\n',
    '\n',
    100 * '?' + '\n'
)

# Choice 2
choice = input('Enter R for Rest or S to Swim: ').lower()

if choice != 'r' and choice != 's':
    print('\n\nSorry, you did not choose correctly.\nThe island explodes.')
    print(gameOver)
    exit
elif choice == 'r':
    print('You choose to wait and rest...')
elif choice == 's':
    print('\n\nSorry, you did not choose correctly.\nThe Loch Ness monster eats your group.')
    print(gameOver)
    exit

print(
    '\n',
    100 * '~' + '\n',
    '\n',
    'You and your crew choose to rest after climbing the mountain.' + '\n',
    'You eat and drink and review the map to see if there is a way to the castle.' + '\n',
    '\n',
    'As the sun hits the Eastern rim of the mountain top, a ship comes into view.' + '\n',
    'Seemingly from nowhere, it is as if it were a ghost.' + '\n',
    '\n',
    100 * '~' + '\n'
)

print(
    '\n',
    100 * '?' + '\n',
    '\n',
    'The ship stops gently at the shore, not a person on deck.' + '\n',
    'A ramp slides down welcoming you and your group onboard.' + '\n',
    '\n',
    'Will you board the ship or will you take caution and remain on land?' + '\n',
    '\n',
    100 * '?' + '\n'
)

# Choice 3
choice = input('Enter B for Board or R to Remain: ').lower()

if choice != 'b' and choice != 'r':
    print('\n\nSorry, you did not choose correctly.\nThe mountain wall collapses on you.')
    print(gameOver)
    exit
elif choice == 'b':
    print('You choose to board the ship...')
elif choice == 'r':
    print('\n\nSorry, you did not choose correctly.\nThe ground turns to lava.')
    print(gameOver)
    exit

print(
    '\n',
    100 * '~' + '\n',
    '\n',
    'You and your crew board the ship and it takes off.' + '\n',
    'It slowly makes way around the island and then into a tunnel underneath it.' + '\n',
    '\n',
    'The ship gently comes to a stop at a stone port with a staircase behind it.' + '\n',
    'You exit the ship with your crew and decide to ascend the steps to the castle.' + '\n',
    '\n',
    100 * '~' + '\n'
)

print(
    '\n',
    100 * '?' + '\n',
    '\n',
    'You reach the top of the spiral staircase and you find 3 doors.' + '\n',
    'One is green, one is red, and one is blue.' + '\n',
    '\n',
    'Which door do you choose?' + '\n',
    '\n',
    100 * '?' + '\n'
)

# Choice 4
choice = input('Enter G for Green or R for Red or B for Blue: ').lower()

if choice != 'g' and choice != 'r' and choice != 'b':
    print('\n\nSorry, you did not choose correctly.\nThe mountain wall collapses on you.')
    print(gameOver)
    exit
elif choice == 'g':
    print('You choose the Green door...')
elif choice == 'r':
    print('\n\nSorry, you did not choose correctly.\nYou open the door and lava pours out.')
    print(gameOver)
    exit
elif choice == 'b':
    print('\n\nSorry, you did not choose correctly.\nYou open the door and water pours out.')
    print(gameOver)
    exit

print('\n',
    '''
    __   _____  _   _  __        _____ _   _ _ 
    \ \ / / _ \| | | | \ \      / /_ _| \ | | |
     \ V / | | | | | |  \ \ /\ / / | ||  \| | |
      | || |_| | |_| |   \ V  V /  | || |\  |_|
      |_| \___/ \___/     \_/\_/  |___|_| \_(_)
    
    '''
)

print(
    '\n',
    100 * '~' + '\n',
    '\n',
    'You and your crew enter the Green door and find a huge room with a banquet table.' + '\n',
    'At the other end of the room is a giant pile of gold and jewels waiting for you.' + '\n',
    '\n',
    'You feast, sleep and collect your treasures before venturing off.' + '\n',
    'You exit the door behind the gold and you are back on your ship sailing home.' + '\n',
    '\n',
    'The End.' + '\n',
    '\n',
    100 * '~' + '\n'
)
