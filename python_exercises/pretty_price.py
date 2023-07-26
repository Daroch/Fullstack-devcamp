import math
def pretty_price(price, rounding):
    if rounding > 1:
        rounding /= 100
        
    return math.floor(price) + rounding

print(pretty_price(34.37,0.95))
