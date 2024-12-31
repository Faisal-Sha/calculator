# Step 1: Basic Arithmetic Operations (will be integrated with Step 2)
def precedence(op: str) -> int:
    """Returns the precedence of the operators."""
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def infix_to_postfix(expression: str) -> list:
    """Converts an infix expression to postfix using the shunting yard algorithm."""
    output = []
    operators = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit() or '.' in token:  # Operand (number)
            output.append(token)
        elif token == '(':  # Left parenthesis
            operators.append(token)
        elif token == ')':  # Right parenthesis
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()  # Pop the '('
        else:  # Operator (+, -, *, /)
            while (operators and precedence(operators[-1]) >= precedence(token)):
                output.append(operators.pop())
            operators.append(token)
    
    while operators:  # Pop remaining operators
        output.append(operators.pop())

    return output

def evaluate_postfix(postfix: list) -> float:
    """Evaluates a postfix expression."""
    stack = []
    for token in postfix:
        if token.isdigit() or '.' in token:  # Operand (number)
            stack.append(float(token))
        else:  # Operator (+, -, *, /)
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                # Handle division by zero
                if operand2 == 0:
                    raise ValueError("Cannot divide by zero")
                stack.append(operand1 / operand2)
    
    return stack[0]  # Final result (single value left in stack)

def calc(expression: str) -> float:
    """Calculates the result of a mathematical expression with operator precedence."""
    # Step 1: Handle basic arithmetic operations first
    expression = expression.replace(' ', '')  # Remove spaces for easier processing

    # Check for basic operations first and perform directly
    if '+' in expression:
        operands = expression.split('+')
        return float(operands[0]) + float(operands[1])
    elif '-' in expression:
        operands = expression.split('-')
        return float(operands[0]) - float(operands[1])
    elif '*' in expression:
        operands = expression.split('*')
        return float(operands[0]) * float(operands[1])
    elif '/' in expression:
        operands = expression.split('/')
        # Handle division by zero
        if float(operands[1]) == 0:
            raise ValueError("Cannot divide by zero")
        return float(operands[0]) / float(operands[1])

    # Step 2: Handle more complex expressions with precedence and parentheses
    postfix = infix_to_postfix(expression)
    return evaluate_postfix(postfix)
