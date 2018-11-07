# solution to level 3 in:
# http://www.pythonchallenge.com/pc/def/equality.html

import re

f = open("re.htm")

encoded_msg = f.read()
f.close()

result = re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+" , encoded_msg)

solution = "".join(result)

print("solution:")
print(solution)
print("link: http://www.pythonchallenge.com/pc/def/" + solution + ".html")

