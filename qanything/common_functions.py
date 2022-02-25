# This function contains snippet of useful code that can used anywhere in the code base.

# External Lib
import numpy as np


def pretty(my_dict, print_key=False, hierarchy_string=""):
    """Prints Dictionary in a Pretty Format.

    Note: This is a recursive function.

    Parameters
    ----------
    my_dict : dict
        Dictionary to be pretty printed
    print_key : bool, optional
        Prints dictionary keys only
    hierarchy_string : str, optional
        string to be append on the left the entire output, only leftmost char
        will be treated as a hierarchy seperator
    """
    if not hierarchy_string:
        next_hierarchy_string = hierarchy_string + " "
    else:
        next_hierarchy_string = hierarchy_string + hierarchy_string[0]

    for key, value in my_dict.items():
        if not print_key:
            if isinstance(value, dict):
                print(hierarchy_string+"***" + str(key) + "***" + '\n')
                pretty(value, print_key, next_hierarchy_string)

            elif isinstance(value, np.ndarray):
                my_prefix_string = hierarchy_string + str(key) + ":\n" + hierarchy_string
                print(my_prefix_string + np.array2string(value, prefix=hierarchy_string) + "\n")

            else:
                print(hierarchy_string + str(key) + ":\n" + hierarchy_string + str(value)+"\n")
        else:
            print(key)
