# Supervised Binning for Recovering Eukaryotic Genomes from Metagenomes

## Overview

This workflow is designed to help recover eukaryotic genomes from metagenomic datasets through supervised binning after running Eukfinder. Below, you will find a detailed guide on how to set up and run the analysis, along with explanations for each step..

### Workflow 


1. Prepare Input Files
You need the following input files before starting:

- A FASTA file of assembled contigs (EUnk.fasta from Eukfinder_short or Eukfinder_long).
- Results from various tools, including Centrifuge, Plast, Blast, Metaxa2, and MyCC.

2. Run Parsing Scripts
Scripts are provided to process results from the tools mentioned above and integrate them into a single analysis pipeline.

3. Generate Output
The pipeline produces two main outputs:

- A FASTA file containing the recovered eukaryotic nuclear genome.
- A FASTA file containing the recovered mitochondrial genome.

## Step-by-Step Instructions

### Step 1. Prepare the Environment

Ensure that you have the following tools and Python libraries installed:

- Python (version 3.6+)
- pandas, Centrifuge, Plast (included in Eukfinder)
- Biopython
  Install via pip install biopython.
- Blast, MyCC, and Metaxa2.

### Step 2. Prepare Input Files

Ensure the assembled contigs file (EUnk.fasta) is located in the TempEukfinder directory.
Copy and rename the file

     ```bash
     cp TempEukfinder/EUnk.fasta Eukfinder_long.fasta
     ```



Step 1. Parse centrifuge result:

Before doing a supervised binning, first run Step0_Eukfinder_long.sh to get classification by Eukfinder_long.
The centrifuge result in the tmps folder and the classified EUnk.fasta will be used for next step.


**INPUT FILE**: (results from Step0_Eukfinder_long.sh)

The centrifuge result in the tmps folder

**OUTPUT FILE**:

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

------------------------------

## Step 2. Run Plast and Parse Plast result

First, run Step2.1_run_Plast.sh
DB=/scratch5/db/Eukfinder/nt2021/nt.fasta


Then, run this python script to parse PLAST result:

   ```sh
   source activate python36-generic
   python3 Step2.2_Parsing_Plast_results.py
   ```


**INPUT FILE**: (results from Step2.1_run_Plast.sh)

Eukfinder_long.PLAST_nt.tsv

**OUTPUT FILE**:

Step2_parsed_Plast_Acc2tax_results.txt


This script will output a table with all the detected eukaryotic contigs:

   ```sh
Eukaryotic species with more than 10 contigs detected by Plast:

                   species  Plast_count
Blastocystis sp. subtype 4         3046
      Blastocystis hominis           33



   ```
       
------------------------------

## Step 3. Run BLAST against Mitochondrial database to detect mitochondrial contigs

Run Step3_Blast_mito.sh

BLASTDB=/scratch5/db/Eukfinder/Mitochondrial


**OUTPUT FILE**:

       Eukfinder_long_BLAST4Mit.out


------------------------------

## Step 4. Depth of coverage and binning

Step4.1_Metaxa2_detection.sh
Use Metaxa2 to detect LSU and SSU rDNA sequences

Step4.2_Depth.sh
Map reads to resulted EUnk.fasta to get depth of coverage file for binning

Step4.3_MyCC
Run MyCC

Step4.4_MaxBin_Metaxa2_Binning.sh
Run MaxBin Metaxa2
Notes: the results from MaxBin and Metaxa2 are not used for supervised binning

Step4.5_Reading_binning_results.py
Parse binning results


   ```sh
   source activate python36-generic
   python3 Step4.5_binning_results.tsv
   ```
------------------------------

## Step 5. Parse all results to generate recovered eukaryotic genomes.


**INPUT FILE**: all the results from previous steps

**OUTPUT FILE**:

eukaryotic nuclear genome and mitochondrial genome in fasta format

   ```sh
   source activate python36-generic
   python3 Step5_Parsing_binning_resutls.py
   ```

