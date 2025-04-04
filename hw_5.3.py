import string

text = input("Введіть рядок: ")

cleaned = ''.join(char for char in text if char not in string.punctuation)

words = cleaned.split()
capitalized = [word.capitalize() for word in words]

hashtag = "#" + ''.join(capitalized)

hashtag = hashtag[:140]

print(hashtag)
