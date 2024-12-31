import sys
import os
# Add the parent directory of 'calculator' to the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../calculator')))

import pytest
from calculator import calc

# Step 1 Tests
def test_addition():
    assert calc('1 + 2') == 3

def test_subtraction():
    assert calc('2 - 1') == 1

def test_multiplication():
    assert calc('2 * 3') == 6

def test_division():
    assert calc('3 / 2') == 1.5

def test_division_by_zero():
    with pytest.raises(ValueError):
        calc('1 / 0')

# Step 2 Tests
# def test_complex_expression_1():
#     assert calc('1 + 1 * 5') == 6

# def test_complex_expression_2():
#     assert calc('(1 + 1) * 5') == 10

# def test_complex_expression_3():
#     assert calc('(2 + 3) * (4 - 1)') == 15

# def test_parentheses_only():
#     assert calc('(2 + 3)') == 5

# def test_operator_precedence():
#     assert calc('3 + 5 * 2') == 13  # 3 + (5 * 2)