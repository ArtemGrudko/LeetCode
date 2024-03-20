import random

#Учитывая целочисленный массив nums, верните наибольший периметр треугольника с ненулевой площадью,
#сформированный из трех из этих длин. Если невозможно сформировать какой-либо треугольник ненулевой площади, верните 0.

def generate_dataset(min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(20)]
def largestPerimetr(nums):
    n = len(nums)
    if n < 3:
        return 0
    nums.sort()
    for i in range(n - 1, 1, -1):
        if nums[i] < (nums[i - 2] + nums[i - 1]):
            return (nums[i - 2] + nums[i - 1] + nums[i])

min_val = 1
max_val = 100

nums = generate_dataset(min_val, max_val)
print(nums)
result = largestPerimetr(nums)
print("perimetr:", result)
