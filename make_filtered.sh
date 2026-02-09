uv run filter.py
uv run generate_ligand_table.py filtered_data
uv run generate_carbene_ligand_table.py filtered_data
Rscript combined_sorted.R
