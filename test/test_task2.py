from tasks.task2 import isPalindrome
import pytest

@pytest.mark.parametrize("x, exception", [("123321", TypeError)])
def test_with_error(x, exception):
    with pytest.raises(exception):
        isPalindrome(x)

@pytest.mark.parametrize("x, result", [(123321, True),
                                       (-123, False)])
def test_isPalindrome(x, result):
    assert isPalindrome(x) == result