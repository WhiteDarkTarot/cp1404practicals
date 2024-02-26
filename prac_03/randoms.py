import random

print(random.randint(5, 20))
# In line 1, I can see a random integer between 5 and 20 (inclusive).
# The smallest number is 5.
# The largest number is 20.

print(random.randrange(3, 10, 2))
# In line 2, I can see a random odd integer between 3 and 9.
# The smallest number is 3.
# The largest number is 9.
# No, because line 2 only generates odd numbers with a stride of 2.

print(random.uniform(2.5, 5.5))
# In line 3, I can see a random floating-point number between 2.5 and 5.5.
# The smallest number is 2.5.
# The largest number is 5.5.

# Code to generate a random number between 1 and 100 inclusive
random_number = random.randint(1, 100)
print(random_number)
