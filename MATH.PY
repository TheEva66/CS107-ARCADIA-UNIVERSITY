# Simple calculator to evaluate 91 to the 143rd power
import sys
result = 91 ** 140000003
sys.set_int_max_str_digits(1000000000)
print(f"91 to the power of 143 is: {result}")