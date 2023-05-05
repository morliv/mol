from util.util import clean_directory
import chem
import rcsb_pdb
import spreadsheetor


def compound_names_smiles():
    spreadsheet = spreadsheetor.get_spreadsheet()
    smiless_with_names_range = "A:B"
    names_smiless_value_range = spreadsheetor.get_values(spreadsheetor.SPREADSHEET_ID, smiless_with_names_range)
    names_smiless = names_smiless_value_range['values']
    names_smiless = list(zip(*names_smiless))
    data_start = 4
    return names_smiless[data_start:]


def compounds(path):
    clean_directory(path)
    for compound in compound_names_smiles():
        chem.sdf(*compound, path=path)


def gene_pdbs(genes, path):
    clean_directory(path)
    return {gene: rcsb_pdb.write_pdb(rcsb_pdb.search_protein(gene), path=path) for gene in genes}
