import re

s = 'State name="New York"'

# Use regular expression pattern to find double-quoted substrings
pattern = r'"[^"]+"'
matches = re.findall(pattern, s)

# Replace double-quoted substrings with placeholders
for i, match in enumerate(matches):
    s = s.replace(match, f'###{i}###')

# Split the string based on '=' and whitespace outside of double quotes
split_parts = re.split(r'=\s+|(?:"[^"]+")', s)

# Replace placeholders with original double-quoted substrings
for i, part in enumerate(split_parts):
    if part.startswith('###') and part.endswith('###'):
        index = int(part[3:-3])
        split_parts[i] = matches[index]

print(split_parts)
