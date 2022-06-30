# Day 55 HTML & URL Parsing in Flask

## Exercise 55-1: Login Decorator Function

For this exercise we will create a decorator which is going to log the name of the function that was called, the arguments it was given and finally the returned output.

### Instructions

1. Write the `login_decorator()` function
2. Use the decorator

### Example Output

```sha
The function called is: some_function


The arguments passed are:

6
['A', 'B', 'C', 'D', 'E', 'F']
[0, 1, 2, 3, 4, 5]
[{0: {'A': 0}}, {1: {'B': 1}}, {2: {'C': 2}}, {3: {'D': 3}}, {4: {'E': 4}}, {5: {'F': 5}}]

The output is:
This Letter: F
This Number: 5
Should Match: {'F': 5}
```

### Hints

1. You can use `function.__name__` to get the name of the function.
2. You'll need to use *args

### Comments

I modified the code to add a white background and shrink the button border for a nicer visual appearance.
