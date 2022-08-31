# Day 76 NumPy & N-Dimensional Arrays

## Overview

For Day 76, we will be working with NumPy.

### Setup

1. Install [Jupyter](https://pypi.org/project/jupyter/)
2. Install [NumPy](https://pypi.org/project/numpy/)

### Instructions

1. Challenge 1:
   1. Use `arange()` to create a vector `a` with values ranging from 10 to 29
   2. OUTPUT:
   ```[10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29]```
2. Challenge 2:
   1. Use Python slicing techniques on `a` to:
      1. Create an array containing only the last 3 values of `a`
      2. Create a subset with only the 4th, 5th, and 6th values
      3. Create a subset of `a` containing all the values except for the first 12 (i.e., [22, 23, 24, 25, 26, 27, 28, 29])
      4. Create a subset that only contains the even numbers
3. Challenge 3:
   1. Reverse the order of the values in `a`, so that the first element comes last
   2. OUTPUT:
   ```[29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]```
4. Challenge 4:
   1. Print out all the indices of the non-zero elements in this array:
   ```[6, 0, 9, 0, 0, 5, 0]```
5. Challenge 5:
   1. Use NumPy to generate a 3x3x3 array with random numbers
6. Challenge 6:
   1. Use `linspace()` to create a vector `x` of size 9 with values spaced out evenly between 0 to 100 (both included)
7. Chalenge 7:
   1. Use `linspace()` to create another vector `y` of size 9 with values between -3 to 3 (both included)
   2. Then plot `x` and `y` on a line chart using Matplotlib
8. Challenge 8:
   1. Use NumPy to generate an array called noise with shape 128x128x3 that has random values
   2. Then use Matplotlib's `imshow()` to display the array as an image
9. Challenge 9:
   1. Multuply `a1` with `b1` using `matmul()`
   2. Then check your work using the `@` multiplier
10. Challenge 10:
    1. What is the data type of img?
    2. What is the shape?
    3. How many dimensions does it have?
    4. What is the resolution of the image?
11. Challenge 11:
    1. Convert the image to B&W
       1. Divide the img values by 255
       2. Multiply the new img values by the given grey values
       3. Show the image
12. Challenge 12:
    1. Manipulate the array to flip the grey image upside down
    2. Rotate the color image
    3. Invert the color image

### Comments

Again, this project was increasingly more difficult as I'm not one to really use data analysis tools in this manner or creating charts. Hopefully, I will be able to understand it a bit better in the future.
