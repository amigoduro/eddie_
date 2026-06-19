import math

x = 0

print("x\t sin(x)\t cos(x)\t tan(x)")

while x <= 10:
    
    sin_x = math.sin(x)    
    cos_x = math.cos(x)   
    tan_x = math.tan(x)
    
    print(round(x, 1), "\t", round(sin_x, 4), "\t", round(cos_x, 4), "\t", round(tan_x, 4))

    
    x = x + 0.2
