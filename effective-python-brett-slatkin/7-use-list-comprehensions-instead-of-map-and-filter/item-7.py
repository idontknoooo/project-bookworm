# List Comprehension vs Map 
squares = [x**2 for x in a]
squares = map(lambda x: x**2, a)
# List Comprehension vs Map & Filter
even_squares = [x**2 for x in a if x % 2 == 0]
even_squares = map(lambda x: x**2, filter(lambda x: x%2==0, a))

# List comprehensions are clearer than the map & filter bulit-in functions because they don't require extra lambda expression.
# Dict & set also support comprehension expression
