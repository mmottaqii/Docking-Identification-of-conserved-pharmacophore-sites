# PyMol Conserved Pharmacophore Sites

This project investigates the role of conserved pharmacophore sites in protein-ligand interactions, leveraging computational tools to quantify and characterize interactions across a diverse dataset of protein-ligand complexes. The ultimate goal is to advance the theoretical understanding of ligand-protein interactions, which could inform the rational design of novel therapeutics.

## Project Overview

![Figure 1: Pharmacophore Sites Interaction](https://github.com/mmottaqii/PyMol_conserved_pharmacophore_sites/blob/main/pictures/Picture_1.png?raw=true)

- **Study Manuscript**: Explore the in-depth analysis in our [published paper](https://github.com/mmottaqii/Docking-Identification-of-conserved-pharmacophore-sites/blob/main/paper/Bioinformatics%20final%20term%20project.pdf).
- **Script Usage**: Access our scripts in the [Script/ directory](https://github.com/mmottaqii/PyMol_conserved_pharmacophore_sites/tree/main/Script).
- **Results Visualization**: View results for different proteins in the [Results/ directory](https://github.com/mmottaqii/PyMol_conserved_pharmacophore_sites/tree/main/Results).

### Key Images from Results

- ![140 Ligands of Aldose Reductase (ALDR) Protein](https://github.com/mmottaqii/PyMol_conserved_pharmacophore_sites/blob/main/pictures/Picture_2.png?raw=true)
- ![Donor Atoms in a Ligand and Pharmacophores](https://github.com/mmottaqii/PyMol_conserved_pharmacophore_sites/blob/main/pictures/Picture_4.png?raw=true)

## Example Results for ALDR (Human Aldehyde Dehydrogenase 1A3, PDB ID: 6TGW)

| N_Ligands = 139 | Label   | Atom Details     | Acceptor H-Bonds | Donor H-bonds | Hydrophobic Interactions |
|-----------------|---------|------------------|------------------|---------------|--------------------------|
| Aldr_atom_1     | Acceptor| /aldr//A/WAT2/O  | NA               | 5             | NA                       |
| Aldr_atom_2     | Acceptor| /aldr//A/WAT3/O  | NA               | 2             | NA                       |
| Aldr_atom_3     | Grease  | /aldr//G/WAT1/C  | NA               | NA            | 266                      |
| Aldr_atom_4     | Grease  | /aldr//G/WAT4/C  | NA               | NA            | 293                      |
| Aldr_atom_5     | Grease  | /aldr//G/WAT5/C  | NA               | NA            | 122                      |
| Aldr_atom_6     | Grease  | /aldr//G/WAT6/C  | NA               | NA            | 259                      |

## Repository Structure

- `assets`: Graphical assets used in the README.
- `data`: Contains datasets used in the study.
- `scripts`: Python scripts used for analysis.
- `results`: Output results including tables and visual data representations.

## Experiment Pipeline

1. Run scripts in `scripts/` to process the pharmacophore data.
2. Use PyMOL and Python for interaction identification and quantification.
3. Analyze the data statistically to identify key pharmacophore sites.
4. Visual representations are generated to complement quantitative findings.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/mmottaqii/PyMol_conserved_pharmacophore_sites/blob/main/LICENSE) file for details.

## Acknowledgments

- **City University of New York**: For providing the academic environment to conduct this research.
- **Protein Data Bank**: Source of the protein-ligand complexes used in this study.
- **Schrödinger LLC**: For providing the PyMOL software used in visual analyses.

Feel free to clone this project and dive into the fascinating world of pharmacophore sites!
