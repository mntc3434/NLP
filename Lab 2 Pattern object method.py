import re
# Compile regex patterns
p1 = re.compile(r'\w+@\w+\.(com|org|net|edu)')  #pattern for email addresses
..
# Match example
email_match = p1.match("steve@apple.com")
if email_match:
    print(email_match.group(0))  # Output: 'steve@apple.com'

# Search example
email_search = p1.search("Email steve@apple.com today.")
if email_search:
    print(email_search.group(0))  # Output: 'steve@apple.com'

# Compile regex pattern for email addresses
p1 = re.compile(r'\w+@\w+\.\w+')  # This will match any domain
# Find all email addresses in the string
email_findall = p1.findall("Email steve@apple.com and bill@msft.com now.")
print(email_findall)  # Output: ['steve@apple.com', 'bill@msft.com']

# Split example
p2 =re.compile("[.?!]+\s+")
split_result = p2.split("Tired? Go to bed! Now!! ")
print(split_result)  # Output: ['Tired?', 'Go', 'to', 'bed!', 'Now!!', '']




