import sys

# Ensure exactly 5 marks are provided
if len(sys.argv) != 6:
    print("Please provide exactly 5 subject marks as command-line arguments.")
    sys.exit(1)

try:
    # Convert command-line arguments to integers
    marks = [int(mark) for mark in sys.argv[1:6]]