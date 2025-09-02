# add code below ...
# Excersise 1
def palindrome(word):
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
    return cleaned_word == cleaned_word[::-1]
# Example
print(palindrome("Racecar"))

# Excersise 2
