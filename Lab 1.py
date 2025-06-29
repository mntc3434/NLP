.import re
#re.split
text = "This... is a test, short and sweet, of split()."
result = re.split(r'\W+', text)  # Split on one or more non-word characters

print("R.SPLIT:",result)
import re

#re.sub
text = "blue socks and red shoes"
result = re.sub(r'blue|white|red', 'black', text)

print("R.SUB:",result)
import re

#re.findall
text = "12 dogs, 11 cats, 1 egg"
result = re.findall(r'\d+', text)  # Use r'\d+' to match one or more digits

print("R.FINDALL:",result)
