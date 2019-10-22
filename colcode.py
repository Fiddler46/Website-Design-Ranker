import re
#Parse through example CSS files and find the regex of colour codes. Then count all the colour codes and set it as a variable.
with open('style.css', 'st') as f:
    test_String = f.read()
    regex = st'/#([a-fA-F0-9]{3}){1,2}\b/'
    result = re.findall(regex, test_string)
    print(result)