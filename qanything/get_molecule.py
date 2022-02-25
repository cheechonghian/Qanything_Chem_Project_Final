# External Lib
import numpy as np

def get_molecule(mol_name, bond_length):

    if mol_name == 'h2':
        mol_symbols = ['H','H']
        coords = np.concatenate((np.array([0,0,0]),np.array([0,0,bond_length])))
        num_elec = 2

    if 'linear_h' in mol_name:
        mol_name_temp_list = mol_name.split('_')
        num_of_h_atoms = int(mol_name_temp_list[1][1])
        mol_symbols = []
        coords = np.array([])
        num_elec = num_of_h_atoms
        for i in range(num_of_h_atoms):
            mol_symbols.append("H")
            coords = np.concatenate((coords,np.array([0,0,i*bond_length])))

    if 'triangle_h3' in mol_name:
        mol_symbols = ['H','H','H']
        coords = np.concatenate((np.array([0,0,0]), np.array([0,0,bond_length]), np.array([np.sqrt(3)*bond_length/2,0,bond_length/2])))
        num_elec = 3

    if 'tetra_h4'in mol_name:
        mol_symbols = ['H','H','H','H']
        xyz_coords = bond_length/np.sqrt(2) * np.array([[1,-1,1],[1,1,-1],[-1,1,1],[-1,-1,-1]])
        temp_coord = [np.array([xyz_coords[i][0], xyz_coords[i][1], xyz_coords[i][2]]) for i in range(4)]
        coords = np.concatenate(temp_coord)
        num_elec = 4

    if 'he2'in mol_name:
        mol_symbols = ['He','He']
        coords = np.concatenate((np.array([0,0,0]),np.array([0,0,bond_length])))
        num_elec = 4

    if 'lih' in mol_name:
        mol_symbols = ['Li','H']
        coords = np.concatenate((np.array([0,0,0]),np.array([0,0,bond_length])))
        num_elec = 4

    # Electronic Charge
    if 'p' in mol_name:
        charge = 1
        num_elec -= 1
    elif 'm' in mol_name:
        charge = -1
        num_elec -= 1
    else:
        charge = 0

    return mol_symbols, coords, charge, num_elec