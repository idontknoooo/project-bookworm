try:
    result = divide(x,y)
except ValueError:
    print("Invalid")
else:
    print("NONE")

# Functions that return None to indicate special meaning are error prone becuase None and other value all evaluate to False in conditional expressions
# Raise exceptions to incidate special situations instead of returning None. Except the calling code to handle exceptions properly when they're documented.
