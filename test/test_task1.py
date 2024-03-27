from tasks.task1 import twoSum
import pytest


@pytest.mark.parametrize("nums, target, result", [([1, 2, 3], 5, [1, 2]),
                                                  ([4, 5, 2], 9, [0, 1]), ])
def test_twoSum(nums, target, result):
    assert twoSum(nums, target) == result


@pytest.mark.parametrize("nums, target, exception", [(123, 5, TypeError)])
def test_with_error(nums, target, exception):
    with pytest.raises(exception):
        twoSum(nums, target)
