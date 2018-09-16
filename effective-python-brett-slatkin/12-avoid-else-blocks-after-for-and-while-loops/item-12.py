# The else blcok after a loop only runs if the loop body didn't encounter a break statement.
# Avoid using else blocks after loops because their behavior isn't intuitive and can be confusing.

for x in []:
    print("Never Runs")
else:
    print("For Else Block!")
