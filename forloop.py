# Let s be a string that contains a sequence of decimal numbers seperated by
# commas, e.g., s = '1.23, 2.43, 3.123'. Write a program that prints the sum of
# numbers in s.

total = 0

for c in [1.23, 2.43, 3.123, 5.78]:
    total += float(c)
print total
