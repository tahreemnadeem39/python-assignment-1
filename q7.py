s = "   Python is fun!   "

# Remove leading and trailing whitespace characters
trimmed_string = s.strip()

# Left justify the string within a field of width 20, using '*' as the fill character
left_justified = trimmed_string.ljust(20, '*')

# Right justify the string within a field of width 20, using '*' as the fill character
right_justified = trimmed_string.rjust(20, '*')

# Printing the results
print(f"Trimmed string: '{trimmed_string}'")
print(f"Left justified: '{left_justified}'")
print(f"Right justified: '{right_justified}'")

