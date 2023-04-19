import re

text = input("Enter the text string: ")
pattern = input("Enter the regex pattern: ")

try:
    regex = re.compile(pattern)
    
    matches = regex.findall(text)
    
    if len(matches) == 0:
        print("No matches found.")
    else:
        print("Matches found:", matches)
        for match in matches:
            print(match)
        
except re.error as e:
    print("Error in regex pattern:", e)
