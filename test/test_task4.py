from tasks.task4 import lengthOfLastWord
import pytest

@pytest.mark.parametrize("s, exception", [(134546 , AttributeError)])
def test_with_error(s, exception):
    with pytest.raises(exception):
        lengthOfLastWord(s)


@pytest.mark.parametrize("s, result", [("123 321", 3),
                                       (" ", 0)])
def test_lengthOfLastWord(s, result):
    assert lengthOfLastWord(s) == result