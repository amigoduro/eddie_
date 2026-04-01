# Importing math module to use sin, cos, tan functions
import math

# Initializing value of x
x = 0
# Printing heading
print("x\t sin(x)\t cos(x)\t tan(x)")

# Using while loop from 0 to 10 with step 0.2
while x <= 10:
    # Calculating sin, cos and tan values
    sin_x = math.sin(x)
    cos_x = math.cos(x)
    tan_x = math.tan(x)

    # Printing values
    print(round(x, 1), "\t", round(sin_x, 4), "\t", round(cos_x, 4), "\t", round(tan_x, 4))

    # Incrementing x by 0.2
    x = x + 0.2
