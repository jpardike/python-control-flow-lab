# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

number_sequence = 0
last_number = 1
number_before_last = 0


for i in range(0, 51):
    number_sequence = last_number + number_before_last
    number_before_last = last_number
    last_number = number_sequence
    print(f'term: {i} / number: {number_sequence}')


