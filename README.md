# Find All Duplicates

Write a function (in python) or method (in Java) that accepts a list of integers and returns a list of only those integers that appear more than once.

## This repository will implement two soultions to this problem

### 1. Using nested loops
This is probably the most simple solution in terms of coding knowledge required. It is particularly straight forward. For each number check all of the numbers after it, and if there is a duplicate, add this number to our new list. *The drawback is that this is O(n^2) complexity.*