user_input = int(input("Enter your age: "))

#save the user input to a variable
age = user_input
#calculate decade
decade = user_input // 10 #this get the integer value of the division
#calculate year
year = user_input % 10 #this mod get the remainder

#Print result to screen
print("Your age are {} You are {} decade and {} year old.".format(age,decade, year))
