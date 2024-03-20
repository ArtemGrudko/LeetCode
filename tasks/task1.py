import random
#TwoSum
#Учитывая массив целых чисел nums и целочисленное целевое значение,
#возвращаем индексы двух чисел таким образом, чтобы они складывались в целевое значение.
#Вы можете предположить, что каждый вход будет иметь ровно одно решение,
# и вы не можете использовать один и тот же элемент дважды.
#Вы можете вернуть ответ в любом порядке.


def generate_dataset(size, min_val, max_val):

    nums = [random.randint(min_val, max_val) for _ in range(size)]
    return nums


def twoSum(nums, target):
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


size = 10
min_val = 1
max_val = 100
target = 10

nums = generate_dataset(size, min_val, max_val)
print("Generated numbers:", nums)
print("target:", target)

result = twoSum(nums, target)
print("Indices for target sum:", result)
