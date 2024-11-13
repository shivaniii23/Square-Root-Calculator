import math
import sys

def calculate_square_root(num):
   if isinstance(num, str):
       raise TypeError("Input must not be string")
   if num < 0:
       raise ValueError("Input must be non-negative")
   return math.sqrt(num)

def main():
    try:
        a = int(sys.argv[1])
        print(f"Square root of {a} is { calculate_square_root(a)}")
    except ValueError as e:
        print("Please enter valid integer")

if __name__ == "__main__":
    main()

