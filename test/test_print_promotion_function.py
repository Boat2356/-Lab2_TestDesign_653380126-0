import pytest
import source.print_promotion_function as print_promotion

# Test scenario 1
def test_print_promotion(capsys):    
    test_cases = [
        (0, "Thank you and see you next time\n"),
        (150, "Thank you and see you next time\n"),
        (499, "Thank you and see you next time\n")
    ]
    for cost, expected in test_cases:
        print_promotion.print_promotion(cost)
        captured = capsys.readouterr()
        assert captured.out == expected

# Test scenario 2
def test_print_promotion2(capsys):    
    test_cases = [
        (500, "Free ice cream cone = 1\n"),
        (699, "Free ice cream cone = 1\n")        
    ]
    for cost, expected in test_cases:
        print_promotion.print_promotion(cost)
        captured = capsys.readouterr()
        assert captured.out == expected

# Test scenario 3
def test_print_promotion3(capsys):    
    test_cases = [
        (700, "Free chocolate cake = 1\n"),
        (1000, "Free chocolate cake = 1\n")        
    ]
    for cost, expected in test_cases:
        print_promotion.print_promotion(cost)
        captured = capsys.readouterr()
        assert captured.out == expected

# Test scenario 4
def test_print_promotion4(capsys):    
    test_cases = [
        (1200, "Free ice cream cone = 1 and Free chocolate cake = 1\n"),
        (2400, "Free ice cream cone = 2 and Free chocolate cake = 2\n"),
        (3600, "Free ice cream cone = 3 and Free chocolate cake = 3\n")
    ]
    for cost, expected in test_cases:
        print_promotion.print_promotion(cost)
        captured = capsys.readouterr()
        assert captured.out == expected

# Test scenario 5
def test_print_promotion(capsys):    
    test_cases = [
        (1300, "Free ice cream cone = 1 and Free chocolate cake = 1\n"),
        (1500, "Free ice cream cone = 1 and Free chocolate cake = 1\n"),
        (2500, "Free ice cream cone = 2 and Free chocolate cake = 2\n"),
        (3500, "Free ice cream cone = 2 and Free chocolate cake = 3\n")
    ]
    for cost, expected in test_cases:
        print_promotion.print_promotion(cost)
        captured = capsys.readouterr()
        assert captured.out == expected

# Test scenario 6
def test_print_promotion(capsys):    
    test_cases = [
        (None, "total_cost must not be null.\n"),
        (-100, "Invalid input. Total cost cannot be negative.\n"),
        ("abc", "Invalid input. Total cost must be a number.\n")
    ]
    for cost, expected in test_cases:
        print_promotion.print_promotion(cost)
        captured = capsys.readouterr()
        assert captured.out == expected