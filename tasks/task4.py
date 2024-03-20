import random
import string
#Учитывая строку s, состоящую из слов и пробелов, верните длину последнего слова в строке.
def generate_string_with_spaces(min_length, max_length):
    return ' '.join([''.join(random.choices(string.ascii_letters, k=random.randint(min_length, max_length))) for _ in range(random.randint(1, 100))])

def lengthOfLastWord(s):
    words = s.split()
    if words:
        print('last  word:', words[-1])
        return len(words[-1])
    else:
        return 0

min_length = 1
max_length = 20
s = generate_string_with_spaces(min_length, max_length)
print("str:", s)

result = lengthOfLastWord(s)
print("length last word:", result)