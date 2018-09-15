# Zip
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters  = count

# Python 3, zip is a lazy generator that products tuple. 
# Python 2, zip returns the full result as a list of tuples
#   izip: can iterator long list
