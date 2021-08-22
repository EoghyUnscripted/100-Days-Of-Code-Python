# Day 8 Function Parameters

## Exercise 8-1: Paint Area Calculator

### Instructions

You are painting a wall. The instructions on the paint can says that **1 can of paint can cover 5 square meters** of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height ✖️ wall width) ÷ coverage per can.

    e.g. Height = 2, Width = 4, Coverage = 5

number of cans = (2 ✖️ 4) ÷ 5

    = 1.6

But because you can't buy 0.6 of a can of paint, the **result should be rounded up** to **2** cans.

**IMPORTANT:** Notice the name of the function and parameters must match those on line 13 for the code to work.

### Code

Use the provided code to complete the exercise.

```python
# WRITE YOUR CODE HERE

n = int(input("Check this number: "))
prime_checker(number=n)
```

### Example Input

```python
test_h = 3
```

```python
test_w = 9
```

### Example Output

    You'll need 6 cans of paint.

### Hint

1. **To round up a number**: [https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python](https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python)
2. Make sure you name your function/parameters the same as when it's called on the last line of code.

## Exercise 8-2: Prime Number Checker

### Instructions

Prime numbers are numbers that can only be cleanly divided by itself and 1.

[https://en.wikipedia.org/wiki/Prime_number](https://en.wikipedia.org/wiki/Prime_number)

**You need to write a function** that checks whether if the number passed into it is a prime number or not.

    e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

![Alt Image](https://cdn.fs.teachablecdn.com/s0gceS97QD6MP5RUT49H)

Here are the numbers up to 100, prime numbers are highlighted in yellow:

![Alt Image](https://cdn.fs.teachablecdn.com/NZqVclSt2qAe8KhTsUtw)

#### Code

Use the provided code to complete the exercise.

```python
# WRITE YOUR CODE HERE

n = int(input("Check this number: "))
prime_checker(number=n)
```

### Example Input 1

    73

### Example Output 1

    It's a prime number.

### Example Input 2

    75

### Example Output 2

    It's not a prime number.

### Hint

1. Remember the modulus: [https://stackoverflow.com/questions/4432208/what-is-the-result-of-in-python](https://stackoverflow.com/questions/4432208/what-is-the-result-of-in-python)
2. Make sure you name your function/parameters the same as when it's called on the last line of code.
3. Use the same wording as the Example Outputs to make sure the tests pass.
