# Supervised Binning for Recovering Eukaryotic Genomes from Metagenomes

## Overview

This workflow is designed to help recover eukaryotic genomes from metagenomic datasets through supervised binning after running Eukfinder. Below, you will find a detailed guide on how to set up and run the analysis, along with explanations for each step.

### Workflow 


1. Prepare Input Files
You need the following input files before starting:

- A FASTA file of assembled contigs (EUnk.fasta from Eukfinder_short or Eukfinder_long).
- Results from various tools, including Centrifuge, Plast, Blast, Metaxa2, Metabat2, and MyCC.

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

   ```sh
   cp TempEukfinder/EUnk.fasta Eukfinder_long.fasta
   ```
#### 2.1 Run Plast against nt database:
Launch the shell run_Plast.sh

DB=/scratch5/db/Eukfinder/nt2021/nt.fasta


#### 2.2 Run BLAST against Mitochondrial database to detect mitochondrial contigs

Run Blast_mito.sh

BLASTDB=/scratch5/db/Eukfinder/Mitochondrial

#### 2.3 Use Metaxa2 to detect LSU and SSU rDNA sequences

Run Metaxa2_detection.sh

#### 2.4 Map reads to resulted EUnk.fasta to get depth of coverage file for binning

Run Depth.sh

**OUTPUT FILE**: Eukfinder_long_EUnk.depth.txt
Eukfinder_long_EUnk.depth.txt file has five columns:
contigName, contigLen, totalAvgDepth, Eukfinder_long_sorted.bam, Eukfinder_long_sorted.bam-var

#### 2.5 Run MyCC


   ```sh
   export PATH=/opt/perun/myCC/Tools:$PATH
   source  /scratch2/software/python2-packages/bin/activate
   cat Eukfinder_long_EUnk.depth.txt | cut -f 1,3 > Eukfinder_long_EUnk_depth_for_binning.txt
   MyCC.py Eukfinder_long.fasta  -a Eukfinder_long_EUnk_depth_for_binning.txt 4mer
   MyCC.py Eukfinder_long.fasta  -a Eukfinder_long_EUnk_depth_for_binning.txt 5mer
   MyCC.py Eukfinder_long.fasta  -a Eukfinder_long_EUnk_depth_for_binning.txt 56mer

   ```

### Step 3. Parse Centrifuge Results

Use the Parsing_centrifuge_results.py script to process Centrifuge results and translate TaxIDs to taxonomy.

   ```bash
   source activate python36-generic
   python3 Parsing_centrifuge_results.py
   ```
Explanation:

-c: Path to the Centrifuge results file.

-o: Output file for parsed results.

The output will contain the eukaryotic species detected and their corresponding counts.


### Step 4. Parse Plast Results


Use the Parsing_Plast_results.py script to process Plast results and annotate them with taxonomy using the acc2tax database.

   ```bash
   source activate python36-generic
   python3 Parsing_Plast_results.py
   ```

Explanation:

-i: Input Plast results file.

-d: Path to the acc2tax database.

-o: Output file for parsed Plast results.

This step annotates Plast results with domain, phylum, genus, and species.

### Step 5: Parse MyCC binning Results

Use the Reading_binning_results.py script to process MyCC binning results and combine the bins into one table.

   ```bash
   source activate python36-generic
   python3 Reading_binning_results.py
   ```

Explanation:

-i: Input fasta file.

-m: Path to the folder containing MyCC results.


### Step 6: Combine All Results and Perform Supervised Binning

Run the main script, Supervised_Binning.py, to combine all parsed results and generate two FASTA files: the nuclear genome and the mitochondrial genome.


   ```bash
   source activate python36-generic
   python3 Supervised_Binning.py
   ```

Explanation:

-i: Input FASTA file.

-c: Parsed Centrifuge results.

-p: Parsed Plast results.

-d: Depth of coverage results.

-b: Binning results.

Outputs:

Eukfinder_long_Blastocystis.fas: Recovered eukaryotic nuclear genome.

Eukfinder_long_Mito_Blastocystis.fas: Recovered mitochondrial genome.


### Step 7: Validate the Results

Check the generated FASTA files:

Nuclear genome (Eukfinder_long_Blastocystis.fas).

Mitochondrial genome (Eukfinder_long_Mito_Blastocystis.fas).

Review the combined results in Combined_binning_results_CPB_Mito.tsv.



