import re

def tokenize_expression(expression: str):
    return re.findall(r'\d+\.?\d*|[+\-*/^()]', expression)


def precedence(op: str) -> int:
    """Returns the precedence of the operators."""
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def infix_to_postfix(tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    operators = []
    
    for token in tokens:
        if token.isdigit():  # Operand
            output.append(token)
        elif token == '(':  # Left parenthesis
            operators.append(token)
        elif token == ')':  # Right parenthesis
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()  # Remove '('
        else:  # Operator
            while (operators and operators[-1] != '(' and
                   precedence[operators[-1]] >= precedence[token]):
                output.append(operators.pop())
            operators.append(token)
    
    while operators:
        output.append(operators.pop())
    
    return output


def evaluate_postfix(postfix):
    stack = []
    for token in postfix:
        if token.isdigit():
            stack.append(float(token))
        else:
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
    return stack[0]


def calc(expression: str):

    """Calculates the result of a mathematical expression with operator precedence."""
    # expression = expression.replace(' ', '')  # Remove spaces for easier processing
    tokens = tokenize_expression(expression)

    # Handle complex expressions with precedence and parentheses using postfix notation
    postfix = infix_to_postfix(tokens)  # Convert infix expression to postfix
    return evaluate_postfix(postfix)  # Evaluate the postfix expression and return the result


