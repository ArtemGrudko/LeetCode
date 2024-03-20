import random
# Учитывая целочисленный массив nums, отсортированный в порядке неубывания,
# удалите дубликаты на месте таким образом, чтобы каждый уникальный элемент появлялся только один раз.
# Относительный порядок элементов должен оставаться неизменным. Затем верните количество уникальных элементов в nums.


def generate_sorted_duplicates(size, min_val, max_val):
    sorted_nums = sorted([random.randint(min_val, max_val) for _ in range(size)])
    return sorted_nums


def removeDublicates(nums):
    print(nums)
    length = len(nums)
    nums[:] = set(nums)
    lenNums = len(nums)
    for i in range(len(nums), length):
        nums.append("_")
    return lenNums, nums

size = 10
min_val = 1
max_val = 10

nums = generate_sorted_duplicates(size, min_val, max_val)
result = removeDublicates(nums)
print("length:", result[0])
print("nums:", result[1])

