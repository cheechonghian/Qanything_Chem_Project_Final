# Exploring the Potential Energy Surface (PES) of a Molecule with a Problem-Inspired Ansatz

### Qanything Chemistry Project

 For Hackaton Challenge QHack 2022

### Team Name: Qanything

### Project Description:

The potential energy surface (PES) of a molecular system describes its energy in terms of geometric parameters such as internuclear distances. For diatomic molecules with only one degree of freedom, i.e. one bond length, the surface is reduced to a potential energy curve or Morse potential. Knowledge of the PES allows the exploration of molecular properties, such as atomization or binding energy, and equilibrium bond lengths for various molecules. For more complex molecules, the optimal equilibrium bond lengths and angles for molecules can be studied. Also, the PES along a particular path can be used to map the energy changes in chemical reactions, allowing study of reaction energies and activation barriers.

![image](https://user-images.githubusercontent.com/39799035/155658637-f9b76e51-ef90-4afa-a46b-fb2cda23efd4.png)


Knowledge of the PES allows the exploration of molecular properties, such as atomization or binding energy, and equilibrium bond lengths for various molecules.

For more complex molecules, the optimal equilibrium bond lengths and angles for molecules can be studied. Also, the PES along a particular path can be used to map the energy changes in chemical reactions, allowing study of reaction energies and activation barriers.

In this project, we explore the PES using a problem-inspired ansatze, Disentangled Unitary Coupled Cluster (UCC) with Singles and Doubles Excitations Rotations. Such UCC methods are notoriously difficult to implement in practice with current NISQ devices due to their need for deep circuits [[1]](http://arxiv.org/abs/2106.13839)  The ansatze are built using Givens rotations [[2]](http://arxiv.org/abs/1910.10130) – simple particle-preserving variational circuits useful for approximating molecular ground states – as building blocks. We will use PennyLane's built in optimization strategies to classically optimise the ansatz to the ground state and map out the ground PES's of simple molecules such as the Hydrogen Molecule H2, Helium Dimer He2 and Lithium Hydride LiH on an exact quantum simulator. After optimizing the ansatz, we will apply various IBM noise models and Error Mitigation techniques from Mitig to study how the PESs are affected by the current NISQ devices.

### Source code:

[Qanything_Chem_Project](https://github.com/cheechonghian/Qanything_Chem_Project)

### Resource Estimate:
The smallest test case, Hydrogen (H2) molecule will require a quantum circuit of at least 4 qubits with 15 independent pauli strings observables. The largest test case, Lithium Hydride (LiH) molecule will require at least 12 qubits with 631 independent pauli strings observables.

### References:

[[1]](http://arxiv.org/abs/2106.13839) Arrazola, J. M., Matteo, O. D., Quesada, N., Jahangiri, S., Delgado, A., & Killoran, N. (2021). Universal quantum circuits for quantum chemistry.

[[2]](http://arxiv.org/abs/1910.10130) Evangelista, F. A., Chan, G. K.-L., & Scuseria, G. E. (2019). Exact parameterization of fermionic wave functions via unitary coupled cluster theory. The Journal of Chemical Physics, 151(24), 244112.
