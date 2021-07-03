# A code statement with # in the front means it is a Python comment.
# We are going to be making our own Mad Libs game! 

## Part 1: Defining Input Variables ############################################
# Let's define some variables you may want to use below, in Mad Libs we want to work with INPUTS in this game, so we want to declare a variable to an input. We can do this by writing:
my_number = input('Please type in a number: ')
print('This is the number you typed in ' + str(my_number))

# Try running this to see what happens!
# What is happening is that we are asking the user of our program to type something and then this value is STORED inside of our variable my_number. The variable my_number is then type casted into a string to concatenate with the rest of the statement Here is an example Mad Lib for you to play with! 
################################################################################
user_name = input("Hey what's your name?: ") # expecting string input
grade = input("What grade are you in? ") # expecting integer input
print() # prints an empty line
print("Introduction Message For You: ")
print('Hi ' + user_name + ', hope you are doing well! :D')
print("Keep working hard and being positive because you're the coolest " + str(grade) +
"th grader. I admire that you are taking the initiative to learn coding this summer. Staying at home can get a little boring, but we can push through this tough time! The cool thing about making Mad Libs is that you can make your own & then ask your family to try it too!")
print() # prints an empty line
print("----------------------------------------------------------")
print()


## Part 2: Walk Through an Example Mad Lib ############################################
# Alright now, we have some variables, let's write print statements that we want
# to print out from our Mad Libs. Keep in mind we will be concatenating (adding) our
# variables together, and using the power of casting to make some Python magic!
# Try making some variables you want to use in your Mad Libs program and make sure to add an input() function that takes in the prompt to ask the user.
# Here's an example below:
################################################################################
print('Let\'s start with an example Mad Lib! :) ') # \ is an escape character in python since the ' you use is the same as the string quotes you are using. You must include the escape character to add the quote ' in your printed string
print("Below, the INPUT variables will ask for your responses & just type them in! ")
print()
print("Example 1: Vacations")
adj1 = input("Please enter an adjective: ")
adj2 = input("Please enter another adjective (different from one above): ")
noun1 = input("Please enter a noun: ")
noun2 = input("Please enter another noun (different from one above): ")
pnoun1 = input("Please enter a plural noun: ")
game = input("Please enter a game: ")
pnoun2 = input("Please enter another plural noun (different from one above): ")
print()
print("Example Mad Libs from your responses: ")
print()
print("A vacation is when you take a trip to some " + adj1 + " with your " + adj2 + " family. Usually you go to some place that is near a/an " + noun1 + " or up on a/an " + noun2 +". A good vacation place is one where you can ride " + pnoun1 + " or play " + game + " or go hunting for " + pnoun2)
print()
print("----------------------------------------------------------")
print()


## Part 3: Making your own Mad Libs #################################################
# Now it is time for your to go on & make your own Mad Libs! Be creative & fun :) 
# Feel free to use the example from above for some inspiration!
print('Let\'s start writing your own Mad Libs below! :) ') 
################################################################################
