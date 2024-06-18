
'''a Python program to test whether a passed letter is a vowel or not'''

def is_vowel(letter):
    vowels = 'aeiouAEIOU'
    return letter in vowels


letter = input("Enter a letter to test: ")
if is_vowel(letter):
    print(letter ," is a vowel.")
else:
    print(letter ," is not a vowel.")