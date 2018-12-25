from enum import Enum

class Operation(Enum):
    add = "+"
    sub = "-"

def detect_operation(op_string: str)->Operation:
    """
    Creates an enum for quick detection of whether addition or subtraction 
    will be used as the operation on a given frequency.

    Args:
        op_string: str single character string that indicates an operation
    Returns: 
        An operation enum for subtraction or addition
    """
    if op_string == '-' or op_string == '+':
        return Operation(op_string)
    else:
        raise TypeError

def detect_integer(op_num: str)->int:
    """
    Gets the integer representation of a string. Used to get the values which will be added by the operation function.
    Args:
        op_num: str The number which will 
    """
    if op_num.isdigit():
        return int(op_num)
    else:
        raise TypeError

def operation():
    pass