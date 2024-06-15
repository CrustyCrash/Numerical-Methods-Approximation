# Find approx value of the cube root of 27

guess = 0.0
cube = 27.0
increment = 0.2
epsilon = 0.1  # error tolerance


while abs(guess**3 - cube) >= epsilon:
    guess += increment

# checking approx value
if abs(guess**3 - cube) >= epsilon:
    print("Failed on the cube root of", cube)
else:
    print(guess, "is close to the cube root of", cube)
