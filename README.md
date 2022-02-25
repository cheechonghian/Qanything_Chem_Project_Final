# Exploring the Potential Energy Surface (PES) of a Molecule with a Problem-Inspired Ansatz

### Qanything Chemistry Project

 For Hackaton Challenge QHack 2022

### Team Name: Qanything

### Project Description:

The potential energy surface (PES) of a molecular system describes its energy in terms of geometric parameters such as internuclear distances. For diatomic molecules with only one degree of freedom, i.e. one bond length, the surface is reduced to a potential energy curve or Morse potential.

![image](https://user-images.githubusercontent.com/39799035/155658637-f9b76e51-ef90-4afa-a46b-fb2cda23efd4.png)


Knowledge of the PES allows the exploration of molecular properties, such as atomization or binding energy, and equilibrium bond lengths for various molecules.

For more complex molecules, the optimal equilibrium bond lengths and angles for molecules can be studied. Also, the PES along a particular path can be used to map the energy changes in chemical reactions, allowing study of reaction energies and activation barriers.

In this project, we use problem-inspired ansatze to map unitary coupled cluster with singles and doubles excitations (UCCSD) PESs. Such UCCSD methods are notoriously difficult to implement in practice with current NISQ devices due to their need for deep circuits [[1]](http://arxiv.org/abs/2106.13839)  The ansatze are built using Givens rotations  [[2]](http://arxiv.org/abs/1910.10130) – simple particle-preserving variational circuits useful for approximating molecular ground states – as building blocks. Creative optimization strategies will be used to obtain molecular energies that map out the PESs of simple molecules H2 and LiH, using both simulated and real hardware. In addition, the effect of noise models on circuits, and in turn the PESs will be studied in this work.

### Source code:

[Qanything_Chem_Project](https://github.com/cheechonghian/Qanything_Chem_Project)

### Resource Estimate:
The smallest test case, Hydrogen (H2) molecule will require a quantum circuit at least 4 qubits with 15 independent pauli strings observables.
The largest test case, Lithium Hydride (LiH) molecule will require at least 12 qubits with 631 independent pauli strings observables.

### References:

[[1]](http://arxiv.org/abs/2106.13839) Arrazola, J. M., Matteo, O. D., Quesada, N., Jahangiri, S., Delgado, A., & Killoran, N. (2021). Universal quantum circuits for quantum chemistry.

[[2]](http://arxiv.org/abs/1910.10130) Evangelista, F. A., Chan, G. K.-L., & Scuseria, G. E. (2019). Exact parameterization of fermionic wave functions via unitary coupled cluster theory. The Journal of Chemical Physics, 151(24), 244112.
