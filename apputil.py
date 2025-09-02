# add code below ...
# Excersise 1
def palindrome(word):
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
    return cleaned_word == cleaned_word[::-1]
# Example
print(palindrome("Racecar"))

# Exercise 2
def parentheses(sequence):
    """
    Checks if the parentheses in the input sequence are balanced.

    Parameters:
        sequence (str): The string to check for balanced parentheses. Non-parentheses characters are ignored.

    Returns:
        bool: True if parentheses are balanced, False otherwise.
    """
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