#!/bin/bash

# Load necessary environment or modules
source $(conda info --base)/etc/profile.d/conda.sh
conda activate metaxa2_env  # Replace with the name of your Conda environment

# Create a directory for Metaxa2 results
mkdir -p Metaxa2_results

# Log the start of the process
echo "==ERR321632_Eukfinder_long.fasta begins=="

# Run Metaxa2 for SSU
metaxa2 --cpu 20 -g SSU -i Eukfinder_long.fasta -o Eukfinder_long_metaxa2_SSU
date

# Run Metaxa2 for LSU
metaxa2 --cpu 20 -g LSU -i Eukfinder_long.fasta -o Eukfinder_long_metaxa2_LSU
date

# Log the completion of the process
echo "==ERR321632_Eukfinder_long.fasta finished=="

# Delete empty files
find . -type f -size 0 -delete

# Move Metaxa2 results to the results directory
mv *_metaxa2_* Metaxa2_results
