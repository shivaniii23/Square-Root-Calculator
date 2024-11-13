from sqrt import calculate_square_root
import pytest

def test_sqrt():
    try:
        assert calculate_square_root(4) == 2
        print("Test case passed: calculate_square_root(4)")
    except AssertionError:
        print("Test case failed: calculate_square_root(4)")

    try:
        assert calculate_square_root(0) == 0
        print("Test case passed: calculate_square_root(0)")
    except AssertionError:
        print("Test case failed: calculate_square_root(0)")

    try:
        assert calculate_square_root(1) == 1
        print("Test case passed: calculate_square_root(1)")
    except AssertionError:
        print("Test case failed: calculate_square_root(1)")

    try:
        assert calculate_square_root(9) == 3
        print("Test case passed: calculate_square_root(9)")
    except AssertionError:
        print("Test case failed: calculate_square_root(9)")

    try:
        assert calculate_square_root(16) == 4
        print("Test case passed: calculate_square_root(16)")
    except AssertionError:
        print("Test case failed: calculate_square_root(16)")

    try:
        assert calculate_square_root(25) == 5
        print("Test case passed: calculate_square_root(25)")
    except AssertionError:
        print("Test case failed: calculate_square_root(25)")

    # Test for non-perfect squares 
    try:
        assert calculate_square_root(2) == pytest.approx(1.41421356237, rel=1e-9)
        print("Test case passed: calculate_square_root(2)")
    except AssertionError:
        print("Test case failed: calculate_square_root(2)")

    try:
        assert calculate_square_root(10) == pytest.approx(3.16227766017, rel=1e-9)
        print("Test case passed: calculate_square_root(10)")
    except AssertionError:
        print("Test case failed: calculate_square_root(10)")

    # Test for negative input 
    try:
        calculate_square_root(-1)
        print("Test case failed: calculate_square_root(-1) did not raise ValueError")
    except ValueError as e:
        print("Test case passed: calculate_square_root(-1) raised ValueError as expected")

    # Test for string input 
    try:
        calculate_square_root("I")
        print("Test case failed: calculate_square_root('I') did not raise TypeError")
    except TypeError as e:
        print("Test case passed: calculate_square_root('I') raised TypeError as expected")

