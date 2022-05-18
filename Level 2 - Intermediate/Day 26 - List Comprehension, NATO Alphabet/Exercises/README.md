# Day 26 List Comprehension, NATO Alphabet

## Exercise 26-1: Squaring Numbers 

### Instructions

You are going to write a List Comprehension to create a new list called `squared_numbers`. This new list should contain every number in the list `numbers` but each number should be squared.

```
e.g. `4 * 4 = 16`
```

```
4 squared equals 16.
```

**DO NOT** modify the List `numbers` directly. Try to use **List Comprehension** instead of a **Loop**.

### Example Input

```python
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

### Example Output

```python
[1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
```

### Hint

1. Use the keyword method for starting the List comprehension and fill in the relevant parts.
2. Make sure the squared_numbers is printed into the console for the code checking to work.

## Exercise 26-2: Filtering Even Numbers 

### Instructions

Using the provided code, you are going to write a List Comprehension to create a new list called `result`. This new list should only contain the even numbers from the list `numbers`.

**DO NOT** modify the List `numbers` directly. Try to use **List Comprehension** instead of a **Loop**.

#### Code

```python
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:



#Write your code 👆 above:

print(result)
```

### Example Input

```python
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

### Example Output

```python
[2, 8, 34]
```

### Hint

1. Use the keyword method for starting the List comprehension and fill in the relevant parts.
2. Even numbers can be divided by 2 with no remainder.
3. Remind yourself of how the modulo operator works.

## Exercise 26-3: Data Overlap 

### Instructions

Take a look inside **file1.txt** and **file2.txt**. They each contain a bunch of numbers, each number on a new line.

You are going to create a list called result which contains the numbers that are common in both files. 

e.g. if file1.txt contained:

```
1
```

```
2
```

```
3
```

and file2.txt contained:

```
2
```

```
3
```

```
4
```

```
result = [2, 3]
```

**IMPORTANT**: The result should be a list that contains **Integers**, not **Strings**. Try to use **List Comprehension** instead of a **Loop**.

### Example Input

file1.txt:
```
3
6
5
8
33
12
7
4
72
2
42
13
```

file2.txt:
```
3
6
13
5
7
89
12
3
33
34
1
344
42
```

### Example Output

```python
[3, 6, 5, 33, 12, 7, 42, 13]
```

### Hint

1. Use the keyword method for starting the List comprehension and fill in the relevant parts.
2. First, you will need to read from the files and create a list using the lines in the files.
3. This method will be really useful: [https://www.w3schools.com/python/ref_file_readlines.asp](https://www.w3schools.com/python/ref_file_readlines.asp)
4. Remember you can check if a value exists in a list using the **in** keyword. [https://www.w3schools.com/python/ref_keyword_in.asp](https://www.w3schools.com/python/ref_keyword_in.asp)
5. Remember you can convert a string to an int using the int() method. [https://www.w3schools.com/python/ref_func_int.asp](https://www.w3schools.com/python/ref_func_int.asp)

## Exercise 26-4 Dictionary Comprehension 1

### Instructions

You are going to use Dictionary Comprehension to create a dictionary called `result` that takes each word in the given sentence and calculates the number of letters in each word.

Try Googling to find out how to convert a sentence into a list of words.

**Do NOT** Create a dictionary directly. Try to use **Dictionary Comprehension** instead of a **Loop**.

#### Code

```python
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:


print(result)
```

### Example Input

```python
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
```

### Example Output

```python
{
    "What": 4, 
    "is": 2, 
    "the": 3, 
    "Airspeed": 8, 
    "Velocity": 8, 
    "of": 2, 
    "an": 2, 
    "Unladen": 7, 
    "Swallow?": 8
}
```

### Hint

1. Use the keyword method for starting the Dictionary comprehension and fill in the relevant parts.
2. You can get a list of the words in a string by using the .split() method: [https://www.w3schools.com/python/ref_string_split.asp](https://www.w3schools.com/python/ref_string_split.asp)

## Exercise 26-5 Dictionary Comprehension 2

### Instructions

You are going to use Dictionary Comprehension to create a dictionary called `weather_f` that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

```
To convert temp_c into temp_f:
```

```
(temp_c * 9/5) + 32 = temp_f
```

**Do NOT** Create a dictionary directly. Try to use **Dictionary Comprehension** instead of a **Loop**.

#### Code

```python
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:



print(weather_f)
```

### Example Input

```python
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
```

### Example Output

```python
{
    "Monday": 53.6, 
    "Tuesday": 57.2, 
    "Wednesday": 59.0, 
    "Thursday": 57.2, 
    "Friday": 69.8, 
    "Saturday": 71.6, 
    "Sunday": 75.2
}
```

### Hint

1. Use the keyword method for starting the Dictionary comprehension and fill in the relevant parts.
2. You can get each of the items from a dictionary using the .items() method: [https://www.w3schools.com/python/ref_dictionary_items.asp](https://www.w3schools.com/python/ref_dictionary_items.asp)
