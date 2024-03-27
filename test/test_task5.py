from tasks.task5 import draw_triangle
import pytest

@pytest.mark.parametrize("height, exception", [("123321", TypeError)])
def test_with_error(height, exception):
    with pytest.raises(exception):
        draw_triangle(height)