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

