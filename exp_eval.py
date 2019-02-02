from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str):
    """Evaluates a postfix expression"""

    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ^ or numbers
    Returns the result of the expression evaluation. 
    Raises a PostfixFormatException if the input is not well-formed"""
    stack = Stack(30)
    tokens = input_str.split(" ")
    if len(tokens) == 0:
        raise PostfixFormatException("Insufficient operands")
    num_val = 0
    num_op = 0
    for token in tokens:
        if is_value(token):
            token = int(token)
            stack.push(token)
            num_val += 1
        elif is_operator(token):
            if stack.size() < 2:
                raise PostfixFormatException("Insufficient operands")
            num_op += 1
            a = stack.pop()
            b = stack.pop()
            result = perform_operation(token, b, a)
            stack.push(result)
    if (num_val == 0) or (num_op == 0):
        raise PostfixFormatException("Invalid token")
    elif (num_val-1) > num_op:
        raise PostfixFormatException("Too many operands")
    return stack.pop()

def is_value(token):
    """Determines if a token can be an integer"""
    try:
        int(token)
        return True
    except ValueError:
        return False

def is_operator(token):
    """Determines if a token is an operator"""
    return token in ['+','-','*','/','**', '>>', '<<']

def perform_operation(operator, a, b):
    """Preforms operations"""
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b != 0:
            return a / b
        else:
            raise ValueError
    elif operator == "**":
        return a ** b
    elif operator == ">>":
        return a >> b
    elif operator == "<<":
        return a << b
    else:
        raise PostfixFormatException("Invalid token")

def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""

    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression """
    stack = Stack(30)
    tokens = input_str.split(" ")
    RPN = ""
    for token in tokens:
        if is_value(token):
            if RPN == "":
                RPN = token
            else:
                RPN = RPN + " " + token
        elif token == "(":
            stack.push(token)
        elif token == ")":
            while stack.peek()!= "(":
                RPN = RPN + " " + stack.pop()
            stack.pop()
        elif is_operator(token):
            while (stack.is_empty() == False) and is_operator(stack.peek()) and has_precedence(token, stack.peek()):
                RPN = RPN + " " + stack.pop()
            stack.push(token)
    while stack.size() > 0:
        RPN = RPN + " " + str(stack.pop())
    return RPN
    
def has_precedence(token1, token2):
    """"""
    # o1 is left-associative and its precedence is less than or equal to that of o2, 
    # o1 is right-associative, and has precedence less than that of o2
    if (precedence(token1) <= precedence(token2) and token1 != "**") or (token1 == "**" and precedence(token1) < precedence(token2)):
        return True
    return False

def precedence(token):
    """Finds the precedence of each operator in order to compare"""
    if token == ">>" or token == "<<":
        return 4
    if token == "**":
        return 3
    if token == "*" or token == "/":
        return 2
    if token == "+" or token == "-":
        return 1

def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)"""
    stack = Stack(30)
    tokens = input_str.split(" ")
    tokens.reverse()
    if tokens == "":
        return tokens
    for token in tokens:
        if is_value(token):
            stack.push(token)
        if is_operator(token) and (stack.size() > 1):
            a = stack.pop()
            b = stack.pop()
            c = a + " " + b + " " + token
            stack.push(c)
    return stack.pop()
