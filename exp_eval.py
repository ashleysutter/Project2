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
#    num_val = 0
#    num_op = 0
    for token in tokens:
        if is_value(token):
            stack.push(token)
#            num_val += 1
        elif is_operator(token):
#            num_op += 1
            a = stack.pop()
            b = stack.pop()
            result = perform_operation(token, b, a)
            stack.push(result)
        '''
        else:
            if (num_val-1) > num_op:
                raise PostFixFormatException("Too many operands")
            elif (num_val-1) < num_op:
                raise PostFixFormatException("Insufficiant operands")'''
    return stack.pop()

def is_value(token):
    try:
        float(token)
        return True
    except ValueError:
        return False

def is_operator(token):
    return token in ['+','-','*','/','**']

def perform_operation(operator, a, b):
    a_num = float(a)
    b_num = float(b)
    if operator == "+":
        return a_num + b_num
    elif operator == "-":
        return a_num - b_num
    elif operator == "*":
        return a_num * b_num
    elif operator == "/":
        return a_num / b_num
    elif operator == "**":
        return a_num ** b_num
    else:
        raise ValueError

def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""

    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression """
    pass


def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)"""
    pass


