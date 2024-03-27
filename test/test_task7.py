from tasks.task7 import climbStairs
import pytest

@pytest.mark.parametrize("nums, result", [(8, 34)])

def test_climbStairs(nums, result):
    assert climbStairs(nums) == result