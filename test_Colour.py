import re
with open('style.css') as f:
    file_contents = f.read()
    regex = r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})'
    result = re.findall(regex, file_contents)
    print(len(set(result)))
