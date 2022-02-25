# Native Lib
import itertools as it

# External Lib
import numpy as np


def generate_excite_index(num_qubits, num_elec):
    # Generate the excitation index for singles and doubles

    # Molecular orbital index
    full_index = np.arange(num_qubits)
    occupied_index = np.arange(num_elec)
    virtual_index = np.setdiff1d(full_index, occupied_index, assume_unique=True)

    # Get the Given Rotation Orbital Index
    A = np.array(list(it.product(occupied_index, virtual_index)))
    single_index = A[np.argsort(A[:,0]-A[:,1])]  # Sort the excitation difference ascendingly (smallest excitation difference first)

    # Get the Double Excitation Index
    combination_occ = np.array(list(it.combinations(occupied_index,2)))
    combination_vir = np.array(list(it.combinations(virtual_index,2)))
    D = np.array(list(it.product(combination_vir, combination_occ)))  # shape of array D: (num_of_double_excitations, 2, 2)
    E = D.reshape(D.shape[0], D.shape[1]*D.shape[2])   # shape of array E: (num_of_double_excitations, 4)
    double_index = np.sort(E, axis=1)  # Sort the excitation index ascendingly, [[l,k,j,i],...] where l < k < j < i

    return occupied_index, single_index, double_index


def generate_disentanglement_order(occupied_index, single_index, double_index):
    # Get the disentanglement index (modified recipe from exact parameterisation of fermionic UCC)

    disentangle_order = []

    # Starting from the last occupied index
    for i in reversed(occupied_index):

        # Get all the single excitations containing that occupied index
        for ind in single_index:
            if i in ind:
                if ind.tolist() not in disentangle_order:
                    disentangle_order.append(ind.tolist())

        # Get all the double excitations containing that occupied index
        for ind in double_index:
            if i in ind:
                if ind.tolist() not in disentangle_order:
                    disentangle_order.append(ind.tolist())

    return disentangle_order


def generate_hardware_efficient_order(num_qubits, num_elec):
    # Get the hardware efficient index for single and doubles rotation

    # Molecular orbital index
    full_index = np.arange(num_qubits)
    occupied_index = np.arange(num_elec)
    virtual_index = np.setdiff1d(full_index, occupied_index, assume_unique=True)

    # Double
    double_index = [occupied_index[-2:]+virtual_index[:2]]

    return disentangle_order