import re
import math

# Tokenizer function to handle numbers, operators, and functions like sin, cos, and tan
def tokenize_expression(expression: str):
    """Tokenizes a mathematical expression into numbers, operators, and functions."""
    # Add functions like sin, cos, and tan into the regular expression
    return re.findall(r'\d+\.?\d*|[+\-*/^()]|sin|cos|tan', expression)



def precedence(op: str) -> int:
    """Returns the precedence of the operators."""
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0


def infix_to_postfix(tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, 'sin': 4, 'cos': 4, 'tan': 4}
    output = []
    operators = []
    
    for token in tokens:
        if token.isdigit() or re.match(r'\d+\.?\d*', token):  # Operand (number)
            output.append(token)
        elif token == '(':  # Left parenthesis
            operators.append(token)
        elif token == ')':  # Right parenthesis
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()  # Remove '('
        elif token in ('sin', 'cos', 'tan'):  # Function (sin, cos, tan)
            operators.append(token)
        else:  # Operator
            while (operators and operators[-1] != '(' and
                   precedence.get(operators[-1], 0) >= precedence.get(token, 0)):
                output.append(operators.pop())
            operators.append(token)
    
    while operators:
        output.append(operators.pop())
    
    return output


def evaluate_postfix(postfix):
    stack = []
    for token in postfix:
        if token.isdigit() or re.match(r'\d+\.?\d*', token):  # Operand (number)
            stack.append(float(token))
        elif token in ('+', '-', '*', '/', '^'):  # Standard operators
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                if operand2 == 0:
                    raise ValueError("Division by zero")
                stack.append(operand1 / operand2)
            elif token == '^':
                stack.append(operand1 ** operand2)
        elif token in ('sin', 'cos', 'tan'):  # Trigonometric functions
            operand = stack.pop()
            # Convert the angle from degrees to radians
            radians = math.radians(operand)
            if token == 'sin':
                stack.append(math.sin(radians))
            elif token == 'cos':
                stack.append(math.cos(radians))
            elif token == 'tan':
                stack.append(math.tan(radians))
    
    return stack[0]


def calc(expression: str):
    """Calculates the result of a mathematical expression with operator precedence."""
    tokens = tokenize_expression(expression)
    postfix = infix_to_postfix(tokens)  # Convert infix expression to postfix
    return evaluate_postfix(postfix)  # Evaluate the postfix expression and return the result
