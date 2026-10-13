import re

m = re.compile(r'a-ZA-Z0-9')
print(bool(str(re.search(m, '0123aZabB'))))