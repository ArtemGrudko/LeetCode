# Учитывая целое число x, верните true, если x является палиндромом, и false в противном случае.

def isPalindrome(x):
    if x < 0:
        return False

    reversedNum = 0
    temp = x

    while temp != 0:
        digit = temp % 10
        reversedNum = reversedNum * 10 + digit
        temp //= 10
    return reversedNum == x


result1 = isPalindrome(12345)
print(result1)

result2 = isPalindrome(123321)
print(result2)

result3 = isPalindrome(-123)
print(result3)