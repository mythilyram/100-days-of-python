# Instructions:
# Write a program that switches the values stored in the variables a and b.
#
# Example Input
# a: 3
# b: 5
# Example Output
# a: 5
# b: 3
#
# Hint
# You might need to make some more variables.
#
a = input("a: ")
b = input("b: ")

####################################
#Logic- use a temp variable C
c=a
a=b
b=c

print("a: " + a)
print("b: " + b)
