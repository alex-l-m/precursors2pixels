from pathlib import Path
import pandas as pd
from rdkit.Chem.rdmolfiles import MolFromSmarts, MolFromSmiles

cyclopropyl = MolFromSmarts("C1CC1")
cyclobutyl = MolFromSmarts("C1CCC1")
nitro = MolFromSmarts("N(~O)(~O)")
chlorine = MolFromSmarts("Cl")
silicon = MolFromSmarts("[Si]")
thiol = MolFromSmarts("[SH]")
sulfonyl = MolFromSmarts("S(~O)(~O)")
excluded = [cyclopropyl, cyclobutyl, nitro, chlorine, silicon, thiol, sulfonyl]

# Filtering predicate
def keep(smiles):
    mol = MolFromSmiles(smiles)
    for substructure in excluded:
        if mol.HasSubstructMatch(substructure):
            return False
    return True


halides_file_name = 'aromatic_halides_with_id.csv'
acids_file_name = 'aromatic_boronic_acids_with_id.csv'
imidazoles_file_name = 'imidazoles_with_id.csv'
file_names = [halides_file_name, acids_file_name, imidazoles_file_name]
smiles_column_names = ["halide_SMILES", "acid_SMILES", "imidazole_SMILES"]

indir = Path('input_data')
outdir = Path('filtered_data')
# Make the output directory if it doesn't already exist
outdir.mkdir(exist_ok=True)
for file_name, smiles_column_name in zip(file_names, smiles_column_names):
    df = pd.read_csv(indir / file_name)
    filtered_df = df[df[smiles_column_name].apply(keep)]
    filtered_df.to_csv(outdir / file_name, index=False)
