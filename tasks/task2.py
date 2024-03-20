import random
# Учитывая целое число x, верните true, если x является палиндромом, и false в противном случае.

def generate_dataset(size, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(size)]

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

size = 10
min_val = 1
max_val = 999

nums = generate_dataset(size, min_val, max_val)
print("Generated numbers:", nums)

for num in nums:
    result = isPalindrome(num)
    print(f"Is {num} a palindrome? {result}")