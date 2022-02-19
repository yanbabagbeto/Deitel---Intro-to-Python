# 5.9 (Palindrome Tester) A string that’s spelled identically backward and forward, like
# 'radar', is a palindrome. Write a function is_palindrome that takes a string and returns
# True if it’s a palindrome and False otherwise. Use a stack (simulated with a list as we did
# in Section 5.11) to help determine whether a string is a palindrome. Your function should
# ignore case sensitivity (that is, 'a' and 'A' are the same), spaces and punctuation.


# Continue while you want to play
# Verify if it is a palindrome
# ask if you want to keep playing


def is_palindrome(word):
    palindrome = True
    word = word.lower()
    for i in range(len(word)):
        if word[i] == word[-(i+1)] and i == (len(word))-1:
            print('It is a palindrome')
            return palindrome
        elif word[i] == word[-(i+1)]:
            continue
        else:
            print(f'Not a palindrome')
            palindrome = False
            return palindrome


def play():
    playing = input('Do you want to play? ')
    while playing != 'n':
        new_word = input('Please enter a new word. ')
        is_palindrome(new_word)
        playing = input('Do you want to play? ')


play()
