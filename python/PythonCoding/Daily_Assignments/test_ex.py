import pytest

# 1. Basic Test Function
def test_sum():
    assert 3 + 5 == 8


# 2. Assertion Failure
def test_uppercase_failure():
    assert "hello".upper() == "hello"


# 3. Fixture Usage
@pytest.fixture
def number_list():
    return [1, 2, 3]

def test_list_length(number_list):
    assert len(number_list) == 3


# 4. Parameterized Test
def square(x):
    return x * x

@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16)
])
def test_square(input, expected):
    assert square(input) == expected


# 5. Exception Handling
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        result = 10 / 0