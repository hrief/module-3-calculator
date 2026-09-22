from unittest.mock import patch

from calculator.main import get_number, main


def test_get_number_valid():
    with patch("builtins.input", return_value="5"):
        assert get_number("Enter number: ") == 5.0


def test_get_number_invalid(capsys):
    with patch("builtins.input", side_effect=["abc", "5"]):
        result = get_number("Enter number: ")

    captured = capsys.readouterr()

    assert result == 5.0
    assert "Invalid input. Please enter a number." in captured.out


def test_main_add(capsys):
    with patch("builtins.input", side_effect=["add", "3", "5", "quit"]):
        main()

    captured = capsys.readouterr()

    assert "Result: 8.0" in captured.out
    assert "Goodbye!" in captured.out


def test_main_invalid_operation(capsys):
    with patch("builtins.input", side_effect=["garbage", "quit"]):
        main()

    captured = capsys.readouterr()

    assert "Invalid operation. Please try again." in captured.out


def test_main_divide_by_zero(capsys):
    with patch("builtins.input", side_effect=["divide", "10", "0", "quit"]):
        main()

    captured = capsys.readouterr()

    assert "Error: Cannot divide by zero" in captured.out