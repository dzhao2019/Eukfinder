# Supervised Binning Steps

## Overview

Below we present list of instructions that lead to recover eukaryotic genomes from metagenomes after running Eukfinder.

The pipeline
1. Parse centrifuge results
2. Run PLAST against nt database 
3. BLAST against Mitochondrial database.
4. Map reads to the selected contigs to get the information about the coverage and use it for run binning tools
5. Refine binning results



## Step 1. Parse centrifuge result:

Before doing a supervised binning, first run Step0_Eukfinder_long.sh to get classification by Eukfinder_long.
The centrifuge result in the tmps folder and the classified EUnk.fasta will be used for next step.


INPUT FILE: (results from Step0_Eukfinder_long.sh)

The centrifuge result in the tmps folder

OUTPUT FILE:

Step1_parsed_centrifuge_results_eukLong.txt

   ```sh
   source activate python36-generic
   python3 Step1_Parsing_centrifuge_results.py
   ```

This script will output a table with all the detected eukaryotic contigs:

   ```sh
Eukaryotic species with more than 10 contigs detected by Centrifuge:

                      species  centrifuge_count
0  Blastocystis sp. subtype 4              3300
1     Cyclospora cayetanensis                15


   ```
