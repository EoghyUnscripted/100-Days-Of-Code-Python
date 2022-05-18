# Day 26 List Comprehension, NATO Alphabet

## Overview

For Day 25, we will start with some exercises to learn how to work with Pandas and csv file data for weather and squirrel census data. The goal is to pull in the data using the Pandas library and use it within our program.

      Exercise 26.1 - Squaring Numbers
      Exercise 26.2 - Filtering Even Numbers
      Exercise 26.3 - Data Overlap
      Exercise 26.4 - Dictionary Comprehension 1
      Exercise 26.5 - Dictionary Comprehension 2

## Project: NATO Alphabet

Using the provided code, we will use list comprehension to convert names to NATO alphabet using an external csv file which stores the NATO Alphabet.

### Instructions

Using the provided `nato_phonetic_alphabet.csv` file, complete the two steps below. The purpose of this lesson is not to just use Pandas and take the "easy" way out and using just the built-in functions. The goal is to use python comprehensions to create your lists and dictionaries.
    
1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
2. Create a list of the phonetic code words from a word that the user inputs
3. Create an input variable and prompt the user for a word to convert to NATO alphabet

### Example Input

```sh
Enter a word to convert to NATO alphabet: NATO
```

#### nato_phonetic_alphabet.csv

```
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

```sh
['November', 'Alfa', 'Tango', 'Oscar']
```

### Comments

One thing that was tricky was understanding how to iterate through the Pandas data_frame. When it is loaded into a variable from a cvs file and printed it shows up as:

```python
{
    'letter': 
        {
            0: 'A', 
            1: 'B', 
            2: 'C',
            3: 'D',
            4: 'E',
            5: 'F',
            6: 'G',
            7: 'H',
            8: 'I',
            9: 'J',
            10: 'K',
            11: 'L',
            12: 'M',
            13: 'N',
            14: 'O',
            15: 'P',
            16: 'Q',
            17: 'R',
            18: 'S',
            19: 'T',
            20: 'U',
            21: 'V',
            22: 'W',
            23: 'X',
            24: 'Y',
            25: 'Z'
        }, 
    'code': 
        {
            0: 'Alfa',
            1: 'Bravo',
            2: 'Charlie',
            3: 'Delta',
            4: 'Echo',
            5: 'Foxtrot',
            6: 'Golf',
            7: 'Hotel',
            8: 'India',
            9: 'Juliet',
            10: 'Kilo',
            11: 'Lima',
            12: 'Mike',
            13: 'November',
            14: 'Oscar',
            15: 'Papa',
            16: 'Quebec',
            17: 'Romeo',
            18: 'Sierra',
            19: 'Tango',
            20: 'Uniform',
            21: 'Victor',
            22: 'Whiskey',
            23: 'X-ray',
            24: 'Yankee',
            25: 'Zulu'
        }
}
```

If we think in terms of JSON for accessing the dictionary {key, value} pairs, we might get thrown into a loop. For example:

1. In JSON, `letters` would be considered element or row 0 and `code` as 1
2. To access the letter `G`, we would have to access it by pointing to `[0][6]`

However, in Pandas, the data is still 2-dimensional. So you access it by getting the row index and the row column.

1. To access `"G"` we would point to `[6][0]` 
2. Or `[6][1]` to get `"Golf"`.
3. Looping through (row, column) on data_frame.iterrow() to get items to a dictionary:
   1. Row automatically updates to the new index where you can access the columns directly to pull the values

#### Demo Notes


