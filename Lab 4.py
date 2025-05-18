....#Sentence Tokenization
text = """Founded in 2002, SpaceX’s mission is to enable humans to become a spacefaring civilization and a multi-planet 
species by building a self-sustaining city on Mars. In 2008, SpaceX’s Falcon 1 became the first privately developed 
liquid-fuel launch vehicle to orbit the Earth."""
# Splits at '.' 
text.split('. ')
#Regular Expression
import re

# Regular expression for sentence delimiters
sentence_delimiter_pattern = r'[፡።.!?]'

# Example usage
text = "This is a sentence. እንኳን ወደ ዚህ ገጽ መጡ፡ How are you?"

# Splitting text into sentences
sentences = re.split(sentence_delimiter_pattern, text)

# Removing any extra whitespace
sentences = [sentence.strip() for sentence in sentences if sentence]

print(sentences)
