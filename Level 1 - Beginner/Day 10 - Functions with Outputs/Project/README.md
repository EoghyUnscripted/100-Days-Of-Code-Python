# Day 10 Calculator Project

## Project 10-1: Combining Dictionaries and Functions

### Instructions

1. Create functions for `add`, `subtract`, `multiply` and `divide` 2 numbers as parameters
2. Create a dictionary using the operator keys `+`, `-`, `*`, and `/` as keys and add, subtract, multiply, and divide as the values
3. Add input variables to get 2 numbers from the user
4. Add input variable for the operation to perform from user
5. Create a call for the appropriate function created in step 1 that the user requested
6. Print an output message with the results

### Example Input

    What is the first number?: 5
    +, -, *, /
    Pick an operation to perform: *
    What is the second number?: 10

### Example Output

    5 * 10 = 50

## Project 10-2: While Loops, Flags, and Recursion

### Instructions

1. Add code to allow user to continue calculating with another number by:
   1. Creating a While Loop to continue the program
   2. Should start the While Loop after accepting the first number
   3. Setting a boolean flag
   4. Using the product or `answer` of the most recent calculation with the new number and operation

2. Adding an input statement that:
   1. Should include the product or `answer` from the most recent calculation
   2. Should ask a user if they want to:
      1. `Y`, continue calculating with previous results
      2. `N`, continue calculating with a new calulation
      3. `Enter`, to exit

3. Shorten the repetitive code by:
   1. Changing the existing code to adjust for the new processes in step 1
   2. Defining a function to implement recursion
   3. **WARNING:** Take care when implementing recursion to avoid infinite loops

### Example Input 1

    What is the first number?: 5
    +, -, *, /
    Pick an operation to perform: *
    What is the next number?: 10

### Example Output 1

    5 * 10 = 50
    Type 'y' to continue calculating with 50, or 'n' to start a new calculation:

### Example Input 2

    Type 'y' to continue calculating with 50, or 'n' to start a new calculation: y
    +, -, *, /
    Pick an operation to perform: +
    What is the next number?: 5

### Example Output 2

    50 + 5 = 55
    Type 'y' to continue calculating with 50, or 'n' to start a new calculation:
