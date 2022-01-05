#at least 8 char long
# contain any sort of letters, numbers, symbols
#has to end with a number

import re
pattern = re.compile(r"[A-Za-z0-9$%@#]{7,}[0-9]")

pwd = 'asdasdasd@#$%2'

b = pattern.fullmatch(pwd)
print(b)