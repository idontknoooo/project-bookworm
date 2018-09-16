# Finally Blocks
handle = open('/tmp/random_data.txt') # May raise IOError
try:
    data = handle.read()              # May raise UnicodeDecodeError
finally:
    handle.close()                    # Always runs after try:

# Else blocks
def load_json_key(data, key):
    try:
	result_dict = json.loads(data)
    except ValueError as e:
	pass
    else:
	return result_dict[key]

# Everything Together
try:
    pass
except ZeroDivisionError as e:
    pass
else:
    pass 
finally:
    pass

# Try/finally compound statement lets you run cleanup code regardless of whether exceptions were raised in the try block
# The else block helps you minimize the amound of code in try blocks and visually distinguish the success case from the try/except blocks
# An else block can be used to perform additional actions after a successful try block but before common cleanup in a finally block.
