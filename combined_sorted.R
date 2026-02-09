# Combine and sort ligands
library(tidyverse)
combinatorial_carbene_ligands <- read_csv('output_data/combinatorial_carbene_ligands.csv.gz', col_types = cols( 
    ligand_identifier = col_character(), 
    ligand_SMILES = col_character(), 
    halide_identifier = col_character(), 
    halide_SMILES = col_character(), 
    imidazole_identifier = col_character(), 
    imidazole_SMILES = col_character() 
)) 
combinatorial_ligands <- read_csv('output_data/combinatorial_ligands.csv', col_types = cols( 
    ligand_identifier = col_character(), 
    ligand_SMILES = col_character(), 
    halide_identifier = col_character(), 
    halide_SMILES = col_character(), 
    acid_identifier = col_character(), 
    acid_SMILES = col_character() 
)) 
sorted_combined_ligands <- bind_rows(combinatorial_carbene_ligands, combinatorial_ligands) |>
    # Sort from smallest ligands to largest, taking the length of the smiles
    # string as a proxy for the size of the ligand
    arrange(str_length(ligand_SMILES))

write_csv(sorted_combined_ligands, 'output_data/combined_sorted_ligands.csv.gz')
