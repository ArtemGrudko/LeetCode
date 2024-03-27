from tasks.task3 import removeDublicates
import pytest

@pytest.mark.parametrize("nums, exception", [(123321, TypeError),
                                             ("321312", TypeError)])
def test_with_error(nums, exception):
    with pytest.raises(exception):
        removeDublicates(nums)

@pytest.mark.parametrize("nums, result", [([1, 1, 2, 2, 3, 3, 3, 4, 5], (5, [1, 2, 3, 4, 5, '_', '_', '_', '_']))])

def test_removeDublicates(nums, result):
    assert removeDublicates(nums) == result