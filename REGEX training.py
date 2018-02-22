import re


string = "whatever.txt"

pattern = r"\..+$"

extension = re.search(pattern, string).group()[1:]

print(extension)