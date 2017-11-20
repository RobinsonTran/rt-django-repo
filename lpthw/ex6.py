types_of_people = 10 # variable for x
x = f"There are {types_of_people} types of people." # 1st verison of string formatting

binary = "binary" # variable for f-stringing stuff
do_not = "don't" # variable for f-stringing stuff
y = f"Those who know {binary} and those who {do_not}." # both previous variables used for y string statement formatting

print(x) # printing "x" with f-string
print(y) # printing "y" with f-string

print(f"I said: {x}") # writing f-string with x statement
print(f"I also said: '{y}'") # writing f-string with y statement

hilarious = False # stored variable
joke_evaluation = "Isn't that joke so funny?! {}" # first part to f-string statment below

print(joke_evaluation.format(hilarious)) # f-string statement with hilarious and joek_evaluation variables used

w = "This is the left side of ..." # simple string tie
e = "a string with a right side."

print(w + e)
