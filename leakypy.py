# Import re module
import re

# Take any string data
string = input("Enter a string value: ")
# Define the searching pattern
pattern = '^[A-Z]'

# match the pattern with input value
found = re.match(pattern, string)

# Print message based on the return value
if found:
    print("The input value is started with the capital letter")
else:
    print("You have to type string start with the capital letter")

password = 'VnDduv#7862-9s8hdv%2hMuh'
aws_akid = 'AKIAIOSFODNN7N0EFXMP'
aws_sk = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYBNA2dBkDTiv'

print(f'{aws_akid}')
