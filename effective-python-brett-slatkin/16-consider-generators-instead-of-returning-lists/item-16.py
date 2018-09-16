# use 'yield' for generator
# Using generators can be clearer than the alternative of returning list of accumulated result
# The iterator returned by a generator produces the set of values passed to 'yield' expressions within the generator function's body
# Generators can produce a sequence of outputs for arbitrarily large inputs because their working memory doesn't include all inputs and outputs.

def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset 
        for letter in line:
            offset += 1 
            if letter == ' ':
                yield offset 
