"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 3
EXERCISE: 3-5 Love Calculator
LEVEL: Beginner

COMMENT:

    There are better ways to do this using lists, but due to progression style of the course,
    I kept things basic to what was already learned along the way.

    I would create another variable to include the search term(s), then split that into elements
    in a list. From there I would combine the names into another list.

    Once that is done, I would use for loops to cycle through the lists and get total counts of
    each letter in the names found in the search terms. This would produce the same score result.

    It would also allow the user or to change the search term if they wanted, or if set in the
    source code, the developer can change the search term without disrupting the program.

"""

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = (name1 + name2).lower()

# Get count of each letter for T, R, U, E from the names
t = combined_names.count('t')
r = combined_names.count('r')
u = combined_names.count('u')
e = combined_names.count('e')

true_count = t + r + u + e  # Total the count of all letters

# Get count of each letter for L, O, V, E from the names
l = combined_names.count('l')
o = combined_names.count('o')
v = combined_names.count('v')
e = combined_names.count('e')

love_count = l + o + v + e  # Total the count of all letters

# Combine the counts from each word
score = true_count + love_count

# Get result statement to output to user
if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif score >= 40 or score <= 50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')
