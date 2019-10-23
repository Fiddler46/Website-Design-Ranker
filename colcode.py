import re
with open('style.css') as f:
    f.readlines()
    #regex = r'/#([a-fA-F0-9]{3}){1,2}\b/'
    result = re.findall(r'/#([a-fA-F0-9]{3}){1,2}\b/', f)
    print(result)
    
#Parse through example CSS files and find the regex of colour codes. Then count all the colour codes and set it as a variable.
