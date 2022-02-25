# Native Lib
import json
import collections

# External Lib
import numpy as np


class NumpyEncoder(json.JSONEncoder):
    # For converting Numpy into JSON array
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def save_to_json(save_filename, save_data):
    print(f'Saving Data to: {save_filename}')
    with open(save_filename, 'w') as jsonfile:
        json.dump(obj          = save_data,
                fp             = jsonfile,
                skipkeys       = False,
                ensure_ascii   = True,
                check_circular = True,
                allow_nan      = True,
                cls            = NumpyEncoder,
                indent         = None,
                separators     = None,
                default        = None,
                sort_keys      = False)


def load_from_json(filename):
    print(f'Loading Data from: {filename}')
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
    return data