# KEY: unlike other languages, there's no 'main' function in a Python file 
# that is called automatically when that file is run. The first line at
# indentation level 0 in the # file will be called and it will go on from there.

# we know __name__ is a built-in variable because of the double underscores.
# In the background, Python assigns __name__ to "__main__".

# Good Python code organisation is to put all function definitions at the top
# and then the if __name__ == "__main__" statement at the bottom.

def func():
    print("func() in one.py")

# So this line will run if one.py is called directly.
print("Top level in one.py")

if __name__ == "__main__":
    # This line will only run if one.py is called directly.
    print("one.py is being run directly!")
else:
    # This line will only run if one.py is NOT called directly.
    print("one.py has been imported")