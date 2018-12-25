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

class OpAction():
    op_integer=0
    op_direction=None

    def __init__(self, op_integer: int = 0, op_direction: Operation = None):
        self.op_integer = op_integer
        self.op_direction = op_direction

    def run(self, input: int=0)->int:
        """
        Runs the operation on a given integer input, defaulting with value 0

        Args:
            input: int The input to the function, if this is not an integer it 
            will still run as if the actual input was 0

        Returns:
            integer of the resulting operation
        """
        if self.op_direction == Operation.add:
            return self.add(input)
        if self.op_direction == Operation.sub:
            return self.sub(input)
        else:
            raise TypeError

    def add(self, input: int)->int:
        return input + self.op_integer
    
    def sub(self, input: int)->int:
        return input - self.op_integer 


def split_string(operation_input: str)->OpAction:
    """
    Creates an OpAction object from a given input string.
    """
    op = detect_operation(operation_input[0])
    integ = detect_integer(operation_input[1:])
    return OpAction(integ, op)

def multi_ops_run(ops_list: [OpAction] = [])->int:
    """
    from a list of ops_actions, this computes from 0, 
    a total of all of the additions that occur in the ops_act list

    Args:
        ops_list: [OpsAction] a list of operations to be performed
    
    Returns:
        integer which is the total addition of all operations found.
    """
    tally = 0
    for ops_act in ops_list:
        tally = ops_act.run(tally)
    return tally