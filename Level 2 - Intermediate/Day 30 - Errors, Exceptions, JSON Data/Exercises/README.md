# Day 30 Errors, Exceptions, JSON Data

## Exercise 30-1: IndexError Handling

### Instructions

We've got some buggy code. Try running the provided code. The code will crash and give you an **IndexError**. This is because we're looking through the list of `fruits` for an index that is out of range.

Use what you've learned about exception handling to **prevent** the program from crashing. If the user enters something that is out of range just print a default output of `"Fruit pie"`.

#### Code

```python
fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")


make_pie(4)
```

### Example Error

```sh
IndexError: list index out of range
```

### Example Output

```sh
Fruit pie   # Default output
```

### Hint

1. You'll need to catch the IndexError exception.
2. You'll need the try, except and else keywords.

## Exercise 30-2: KeyError Handling

### Instructions

We've got some buggy code, try running the provided code. The code will crash and give you a **KeyError**. This is because some of the posts in the `facebook_posts` don't have any `"Likes"`.

Use what you've learned about exception handling to **prevent** the program from crashing.

#### Code

```python
facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    total_likes = total_likes + post['Likes']


print(total_likes)
```

### Example Error

```sh
KeyError: 'Likes'   # No post['Likes'] key found
```

### Example Output

```sh
86  # Counts 0 when post['Likes'] is missing from data
```

### Hint

1. You'll need to catch the KeyError exception.
2. Posts without any likes can be counted as 0 likes.

## Exercise 30-3: Exception Handling with the NATO Alphabet Project

### Instructions

Using the provided code and csv data file, write exception handling for KeyError.

1. The code should alert user to use only alphabetical letters for their input
2. The code should loop until there are no errors detected



### Example Input

```sh
Enter a word: 6643574
```

#### exercise30-3.csv

```csv
letter,code
A,Alfa
B,Bravo
C,Charlie
D,Delta
E,Echo
F,Foxtrot
G,Golf
H,Hotel
I,India
J,Juliet
K,Kilo
L,Lima
M,Mike
N,November
O,Oscar
P,Papa
Q,Quebec
R,Romeo
S,Sierra
T,Tango
U,Uniform
V,Victor
W,Whiskey
X,X-ray
Y,Yankee
Z,Zulu
```

### Example Output

```txt
Only letters in the alphabet are allowed.
```
