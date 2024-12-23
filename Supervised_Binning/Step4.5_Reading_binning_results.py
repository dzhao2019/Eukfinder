"""
Combine binning results from Maxbin, Metabat2, and MyCC into one table.
Version 1.1.0, Dec 17, 2024
Author: D.Z.

================================================
python3 combine_binning_results.py [-i <fasta_file> -m <MyCC directory>]
================================================

This script performs the following steps:
1. Parses binning results from Maxbin, Metabat2, and MyCC directories.
2. Combines the parsed results into a single table.
3. Outputs the combined table in TSV format.

Output Example:
    seqID         MaxBin     Metabat       MyCC_5mer   MyCC_4mer
    NODE_1        bin.001    bin.002       5mer_001    4mer_001
    NODE_2        bin.003    bin.004       5mer_002    4mer_002
"""

import os
import argparse
from Bio import SeqIO
import pandas as pd


def parse_binning_results(prefix, folder, file_pattern, column_name):
    """
    Parse binning results from files matching a specific prefix and pattern.

    Args:
        prefix (str): Prefix of binning result files (e.g., "maxbin2").
        folder (str): Directory containing binning result files.
        file_pattern (str): File extension pattern (e.g., "fasta", "fa").
        column_name (str): Name of the resulting column in the DataFrame.

    Returns:
        pd.DataFrame: DataFrame containing parsed binning results.
    """
    print(f"Parsing {column_name} results...")
    result_dict = {}

    # Iterate through files in the folder and filter by prefix and pattern
    for file in os.listdir(folder):
        if file.startswith(prefix) and file.endswith(file_pattern):
            cluster = file.split('.')[-2]  # Extract cluster identifier
            print(f"  Processing file: {file}")
            for record in SeqIO.parse(os.path.join(folder, file), 'fasta'):
                result_dict[record.id] = cluster

    print(f"  Total contigs parsed for {column_name}: {len(result_dict)}")
    return pd.DataFrame.from_dict(result_dict, orient='index', columns=[column_name])


def parse_mycc_results(mycc_dir):
    """
    Parse MyCC binning results from directories organized by k-mer types.

    Args:
        mycc_dir (str): Directory containing MyCC binning result subdirectories.

    Returns:
        pd.DataFrame: Combined DataFrame of MyCC results for all k-mers.
    """
    print("Parsing MyCC results...")
    combined_df = pd.DataFrame()

    # Walk through the MyCC directory structure to locate relevant directories
    for root, dirs, _ in os.walk(mycc_dir):
        for dir in dirs:
            if "mer" in dir:
                kmer = dir.split('_')[-3]  # Extract k-mer type (e.g., "5mer", "4mer")
                mycc_dict = {}
                dir_path = os.path.join(root, dir)
                for file in os.listdir(dir_path):
                    if file.startswith("Cluster") and file.endswith("fasta"):
                        cluster = file.split('.')[1]  # Extract cluster identifier
                        for record in SeqIO.parse(os.path.join(dir_path, file), 'fasta'):
                            mycc_dict[record.id] = f"{kmer}_{cluster}"

                # Create a DataFrame for the current MyCC directory and merge it
                df = pd.DataFrame.from_dict(mycc_dict, orient='index', columns=[f"MyCC_{kmer}"])
                combined_df = pd.concat([combined_df, df], axis=1)

    print(f"  Total contigs parsed for MyCC: {combined_df.shape[0]}")
    return combined_df


def main(fasta_file, mycc_directory):
    """
    Main function to parse and combine binning results.

    Args:
        fasta_file (str): Path to the input fasta file.
        mycc_directory (str): Path to the directory containing MyCC results.

    Outputs:
        A combined TSV file containing binning results from all tools.
    """
    # Parse binning results for MaxBin and Metabat2
    maxbin_df = parse_binning_results("maxbin2", "Binning_results", "fasta", "MaxBin")
    metabat_df = parse_binning_results("metabat2", "Binning_results", "fa", "Metabat")

    # Parse MyCC binning results
    mycc_df = parse_mycc_results(mycc_directory)

    # Combine all results into a single DataFrame and fill missing values
    combined_results = pd.concat([maxbin_df, metabat_df, mycc_df], axis=1).fillna("unbinned")

    # Output the combined results to a TSV file
    output_file = "binning_results.tsv"
    print(f"Writing combined results to {output_file}...")
    combined_results.to_csv(output_file, sep='\t', index_label="seqID")
    print("Finished.")


if __name__ == '__main__':
    # Define command-line arguments
    parser = argparse.ArgumentParser(
        description="Combine binning results from MaxBin, Metabat2, and MyCC into one table.",
        epilog="Usage: python3 combine_binning_results.py [-i <fasta_file> -m <MyCC directory>]"    )
    parser.add_argument( "-i", "--input", help="Input fasta file before binning", required=False, default="Eukfinder_long.fasta" )
    parser.add_argument( "-m", "--mycc", help="Input directory containing all MyCC results", required=False, default="."  )
    args = parser.parse_args()

    # Execute the main function with parsed arguments
    main(args.input, args.mycc)
