# List vs Generator
value = [len(x) for x in open('/tmp/my_file.txt')] # List 
value = (len(x) for x in open('/tmp/my_file.txt')) # Generator

# 1. List comprehensions can cause problems for large input by using too much memory
# 2. Generator expressions avoid memory issues by proudicng outputs one at a time as an iterator 
# 3. Convert generator to list is also quick
