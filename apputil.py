# add code below ...
# Excersise 1
def palindrome(word):
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
    return cleaned_word == cleaned_word[::-1]
# Example
print(palindrome("Racecar"))

# Excersise 2
def parentheses(sequence):
    balance = 0
    for char in sequence:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance < 0:
            return False
    return balance == 0
# Example
print(parentheses("((()))"))
print(parentheses("(blah)()()()"))
print(parentheses("((((((())"))