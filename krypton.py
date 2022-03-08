# Read in how many elements we need to help Superman identify
elements = int(input())
for t in range(elements):
    # Read in the value of the element
    value = int(input())
    atomic_value = value**2;
    # Print the square of the element so that Superman can look it up on the periodic table
    print(atomic_value)
