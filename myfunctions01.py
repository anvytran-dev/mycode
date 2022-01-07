#!/usr/bin/env python3


## Write a Python function to sum all the numbers in a list.

def sumNumbersInList(listOfNumbers):
    sum = 0
    for num in listOfNumbers:
        sum +=num
    return sum

## Write a Python function to find the Max of three numbers.

def findMax(listOfNumbers):
    max = listOfNumbers[0]
    for num in listOfNumbers:
        if num > max:
            max = num
    return max

## Write a Python program to reverse a string.

def reverseString(string):
    reversed = string[::-1]
    return reversed

## Write a Python function to check whether a number is in a given range.

def isInRange(num):
    a = 12
    b = 20
    if num in range(12, 20):
        print(f"Yes. {num} is in range from {a}-{b}.")
    else:
        print(f"No. {num} is not in range from {a}-{b}.")

def main():

   print(sumNumbersInList([8, 2, 3, 0, 7]))
   print(findMax([12, 5, 9, 25, 4]))
   print(reverseString('abc'))
   isInRange(9)
    

main()
