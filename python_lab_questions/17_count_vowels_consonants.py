# Return a dictionary containing vowel and consonant counts.
def count_letters(text):
    vowels = consonants = 0
    for char in text.lower():
        if char.isalpha():
            if char in 'aeiou':
                vowels += 1
            else:
                consonants += 1
    return {'vowels': vowels, 'consonants': consonants}

if __name__ == '__main__':
    print(count_letters(input('Enter a string: ')))
