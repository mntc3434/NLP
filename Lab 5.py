import re

def normalize_char_level_mismatch(input_token):
    # Define replacements as a dictionary
    replacements = {
        '[ሃኅኃሐሓኻ]': 'ሀ',
        '[ሑኁዅ]': 'ሁ',
        '[ኂሒኺ]': 'ሂ',
        '[ኌሔዄ]': 'ሄ',
        '[ሕኅ]': 'ህ',
        '[ኆሖኾ]': 'ሆ',
        '[ሠ]': 'ሰ',
        '[ሡ]': 'ሱ',
        '[ሢ]': 'ሲ',
        '[ሣ]': 'ሳ',
        '[ሤ]': 'ሴ',
        '[ሥ]': 'ስ',
        '[ሦ]': 'ሶ',
        '[ዓኣዐ]': 'አ',
        '[ዑ]': 'ኡ',
        '[ዒ]': 'ኢ',
        '[ዔ]': 'ኤ',
        '[ዕ]': 'እ',
        '[ዖ]': 'ኦ',
        '[ጸ]': 'ፀ',
        '[ጹ]': 'ፁ',
        '[ጺ]': 'ፂ',
        '[ጻ]': 'ፃ',
        '[ጼ]': 'ፄ',
        '[ጽ]': 'ፅ',
        '[ጾ]': 'ፆ',
        # Normalizing labialized characters
        '(ሉ[ዋአ])': 'ሏ',
        '(ሙ[ዋአ])': 'ሟ',
        '(ቱ[ዋአ])': 'ቷ',
        '(ሩ[ዋአ])': 'ሯ',
        '(ሱ[ዋአ])': 'ሷ',
        '(ሹ[ዋአ])': 'ሿ',
        '(ቁ[ዋአ])': 'ቋ',
        '(ቡ[ዋአ])': 'ቧ',
        '(ቹ[ዋአ])': 'ቿ',
        '(ሁ[ዋአ])': 'ኋ',
        '(ኑ[ዋአ])': 'ኗ',
        '(ኙ[ዋአ])': 'ኟ',
        '(ኩ[ዋአ])': 'ኳ',
        '(ዙ[ዋአ])': 'ዟ',
        '(ጉ[ዋአ])': 'ጓ',
        '(ደ[ዋአ])': 'ዷ',
        '(ጡ[ዋአ])': 'ጧ',
        '(ጩ[ዋአ])': 'ጯ',
        '(ጹ[ዋአ])': 'ጿ',
        '(ፉ[ዋአ])': 'ፏ',
        '[ቊ]': 'ቁ',
        '[ኵ]': 'ኩ'
    }

    # Apply each replacement
    for pattern, replacement in replacements.items():
        input_token = re.sub(pattern, replacement, input_token)

    return input_token

# Example sentences
sentences = [
    "እንኳን ወደ ዚህ ገጽ መጡ፡ እንዴት ነህ?",
    "በልቱዋል የተለየ ነው፡ ወይስ በልቱአል?",
    "እንስሳት በጣም ውድ ናቸው፡ ምን እንደሚኖር ይመለከታል?"
]

# Normalize and print each sentence
for sentence in sentences:
    normalized_sentence = normalize_char_level_mismatch(sentence)
    print(normalized_sentence)
