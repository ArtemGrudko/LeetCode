import random

#Учитывая целочисленный массив nums, верните наибольший периметр треугольника с ненулевой площадью,
#сформированный из трех из этих длин. Если невозможно сформировать какой-либо треугольник ненулевой площади, верните 0.


def largestPerimetr(nums):
    n = len(nums)
    if n < 3:
        return 0
    nums.sort()
    for i in range(n - 1, 1, -1):
        if nums[i] < (nums[i - 2] + nums[i - 1]):
            return (nums[i - 2] + nums[i - 1] + nums[i])

