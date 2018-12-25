from collections import Counter

def box_has_n_repeat(repeat_val: int, box_counter: Counter)->bool:
    """
    Takes in the counter representation of a box and detects the checksum 
    contains 1 or more letters repeated

    Args:
        repeat_val: int the integer that we are checking for n number of 
        repeats
        box_counter: the Counter object representation of a box
    Returns:
        Boolean indicating if atleast 1 letter in a box's id repeats the same 
        number of times as the given input repeat_val
    """
    for _letter,count in box_counter.items():
        if count == repeat_val:
            return True
    return False


def box_2_3_counts(box_counter: Counter)->dict:
    box_additions = {2:0, 3: 0}
    if box_has_n_repeat(2, box_counter):
        box_additions[2] = 1
    if box_has_n_repeat(3, box_counter):
        box_additions[3] = 1
    return box_additions