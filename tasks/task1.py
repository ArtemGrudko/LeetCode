#TwoSum
#Учитывая массив целых чисел nums и целочисленное целевое значение,
#возвращаем индексы двух чисел таким образом, чтобы они складывались в целевое значение.
#Вы можете предположить, что каждый вход будет иметь ровно одно решение,
# и вы не можете использовать один и тот же элемент дважды.
#Вы можете вернуть ответ в любом порядке.


def twoSum(nums, target):
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []



nums1 = [2,1,8,3]
target1 = 9
result1 = twoSum(nums1, target1)
print(result1)

nums2 = [1,1,1,1,12]
target2 = 5
result2 = twoSum(nums2, target2)
print(result2)

nums3 = [3,5,9,21,543,65,8]
target3 = 11
result3 = twoSum(nums3, target3)
print(result3)