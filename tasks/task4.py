#Учитывая строку s, состоящую из слов и пробелов, верните длину последнего слова в строке.

def lengthOfLastWord(s):
    words = s.split()
    if words:
        print('last  word:', words[-1])
        return len(words[-1])
    else:
        return 0

s = "Hello world"
result = lengthOfLastWord(s)
print(result)