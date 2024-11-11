from sqrt import calculate_square_root
import pytest

def test_sqrt(): 
    assert calculate_square_root(4) == 2
    assert calculate_square_root(0) == 0
    assert calculate_square_root(1) == 1 
    assert calculate_square_root(9) == 3 
    assert calculate_square_root(16) == 4 
    assert calculate_square_root(25) == 5 
    # Test for non-perfect squares 
    assert calculate_square_root(2) == pytest.approx(1.41421356237, rel=1e-9) 
    assert calculate_square_root(10) == pytest.approx(3.16227766017, rel=1e-9) 
    # Test for negative input 
    try: 
        calculate_square_root(-1) 
    except ValueError as e: 
        assert str(e) == "Input must be non-negative"
    # Test for string input 
    try: 
        calculate_square_root("I") 
    except TypeError as e: 
        assert str(e) == "Input must not be string"

