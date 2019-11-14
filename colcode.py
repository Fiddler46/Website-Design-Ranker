import re
with open('style.css') as f:
    file_contents = f.read()
    regex = r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})'
    result = re.findall(regex, file_contents)
<<<<<<< HEAD
    print(result)
=======
    print(len(set(result)))
>>>>>>> 63c0a83cd6cc175e5b8f9fa16c39c7578f696fde
    
#Parse through example CSS files and find the regex of colour codes. Then count all the colour codes and set it as a variable.
