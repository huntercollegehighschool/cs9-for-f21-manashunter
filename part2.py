"""
******
PART 2
******
Write a program that asks the user to enter a positive integer n. The program will then print the sum of the first n positive cubes.

For example, if the user types in 4, the program should print 100 (since 1^3 + 2^3 + 3^3 + 4^3 = 100).
"""

#write your code here
number = int(input("What number are you looking for? "))

sum = 0

for i in range(1,number+1):
  i = i * i * i
  sum = sum + i

print(sum)