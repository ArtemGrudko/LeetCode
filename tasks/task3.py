import random
# Учитывая целочисленный массив nums, отсортированный в порядке неубывания,
# удалите дубликаты на месте таким образом, чтобы каждый уникальный элемент появлялся только один раз.
# Относительный порядок элементов должен оставаться неизменным. Затем верните количество уникальных элементов в nums.




def removeDublicates(nums):
    print(nums)
    length = len(nums)
    nums[:] = set(nums)
    lenNums = len(nums)
    for i in range(len(nums), length):
        nums.append("_")
    return lenNums, nums

print(removeDublicates([1,1,2,2,3,3,3,4,5]))