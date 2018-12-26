from collections import Counter, defaultdict

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
    """
    Takes in the counter representation of a box and detects the checksum 
    if it contains 2 or 3 repeated letters


    """
    box_additions = {2:0, 3: 0}
    if box_has_n_repeat(2, box_counter):
        box_additions[2] = 1
    if box_has_n_repeat(3, box_counter):
        box_additions[3] = 1
    return box_additions

def dict_adder(dict_a: dict, dict_b)->dict:
    """
    Adds the contents of two dictionaries that have keys 2 and 3 together
    """
    dict_a[2] = dict_a[2] + dict_b[2]
    dict_a[3] = dict_a[3] + dict_b[3]
    return dict_a

def manhattan_vect_strings(str_a: str, str_b: str)->[int]:
    """
    Function that finds the edit vector for two strings, for a given element 0 
    means the two strings have the same character in the same place. For a 1 
    this means the characters differ.

    Args:
        str_a: str First string to be considered equal length to str_b
        str_b: str Second string to be considered equal length to str_a
    Returns
        A list of integers 0 or 1 for each space 
    """
    if len(str_a) == len(str_b):
        edit_vec = []
        for index in range(0,len(str_a)):
            if str_a[index] == str_b[index]:
                edit_vec.append(0)
            else:
                edit_vec.append(1)
        return edit_vec
    else:
        raise ValueError

def manhattan_dist(str_a: str, str_b: str)->int:
    return sum(manhattan_vect_strings(str_a, str_b))

def manhattan_grid(box_ids: [str])->defaultdict:
    track_id_grid = defaultdict(list)
    for box_id_0 in range(0,len(box_ids)):
        for box_id_1 in range(box_id_0+1, len(box_ids)):
            track_id_grid[manhattan_dist(box_ids[box_id_0],box_ids[box_id_1])].append([box_id_0,box_id_1])
    return track_id_grid

def get_smallest_key(box_ids: [str])->[int]:
    manhattan_grids = manhattan_grid(box_ids)
    keys = sorted(list(manhattan_grids.keys()))
    return manhattan_grids[keys[0]][0]

def get_manhattan_edit(box_ids: [str])->str:
    indices = get_smallest_key(box_ids)
    nstr = box_ids[indices[0]]
    edit = manhattan_vect_strings(box_ids[indices[0]], box_ids[indices[1]])
    while(True):
        try:
            ind = edit.index(1)
            nstr = nstr[:ind] + nstr[ind+1:]
            edit = edit[:ind] + edit[ind+1:]
        except ValueError:
            break
    
    return nstr
