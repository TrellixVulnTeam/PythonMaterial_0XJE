import nose
from mymath import add, divide


def test_add_integers():
    assert add(5, 3) == 8


def test_add_integers_zero():
    assert add(3, 0) == 3


def test_add_floats():
    assert add(1.5, 2.5) == 4


def test_add_strings():
    nose.tools.assert_raises(AssertionError, add, "paul", "carol")


def test_divide_integers_even():
    assert divide(2, 10) == 0.2


def test_divide_integers_repetant():
    nose.tools.assert_almost_equal(divide(1, 3), 0.33333333, 7)


if __name__ == "__main__":
    nose.run()
