# Command-Line Calculator

A command-line calculator application written in Python. The application provides a continuous interface that allows users to perform basic arithmetic operations with input validation and error handling.

## Setup

Clone the repository and navigate to the project directory:

git clone https://github.com/hrief/module-3-calculator.git
cd calculator_cli


Create a virtual environment:
```
python -m venv .venv
```

Activating the virtual environment on Windows:

```
.venv\Scripts\Activate.ps1
```

Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

Run the calculator from the project root:

```
python -m calculator.main
```

The calculator will prompt for an operation and two numbers:

```text
Calculator
Operations: add, subtract, multiply, divide
Type 'quit' to exit.

Enter operation: add
Enter first number: 3
Enter second number: 5
Result: 8.0
```

Enter `quit` at the operation prompt to exit the application.

## Testing

Run all tests with:

```
python -m pytest
```