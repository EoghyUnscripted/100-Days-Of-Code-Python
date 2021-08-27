# Day 13 Debugging

## Exercise 13-1: Odd or Even

### Instructions

1. Evaluate the provided code
2. Spot the problems
3. Modify the code to fix the bugs

#### Code

```python
number = int(input("Which number do you want to check?"))

if number % 2 = 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
```

## Exercise 13-2: Leap Year

### Instructions

1. Evaluate the provided code
2. Spot the problems
3. Modify the code to fix the bugs

#### Code

```python
year = input("Which year do you want to check?")

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
```

## Exercise 13-3: FizzBuzz

### Instructions

1. Evaluate the provided code
2. Spot the problems
3. Modify the code to fix the bugs

#### Code

```python
for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])
```
