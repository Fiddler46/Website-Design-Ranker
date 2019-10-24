import re
with open('style.css') as f:
    file_contents = f.read()
    regex = r'/#([a-fA-F0-9]){3}(([a-fA-F0-9]){3})?\b/'
    result = re.findall(regex, file_contents)
    print(result)
    
#Parse through example CSS files and find the regex of colour codes. Then count all the colour codes and set it as a variable.
