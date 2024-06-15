import numpy as np
# Find approx value of the cube root of 27

guess = 0.0
cube = 27.0
increment = 0.2
epsilon = 0.1  # error tolerance

# Method 1 using While loop
while abs(guess**3 - cube) >= epsilon:
    guess += increment

# checking approx value
if abs(guess**3 - cube) >= epsilon:
    print("Approx values using While loop : ")
    print("Failed on the cube root of", cube)
else:
    print("Approx values using While loop : ")
    print(guess, "is close to the cube root of", cube)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Method 2 using For loop
print("Approximating values of cube using for loop")
for i in np.arange(0.0,27.0,0.2):
    if abs(i**3 - cube) < epsilon:
        print("Guess = ", guess, " is close to cube root of ", cube)
        break


