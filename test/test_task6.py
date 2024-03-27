from tasks.task6 import largestPerimetr
import pytest

@pytest.mark.parametrize("nums, exception", [("123321", AttributeError),
                                             (123213, TypeError)])
def test_with_error(nums, exception):
    with pytest.raises(exception):
        largestPerimetr(nums)

@pytest.mark.parametrize("nums, result", [([1,2,3,4,5], 12)])

def test_largestPerimetr(nums, result):
    assert largestPerimetr(nums) == result