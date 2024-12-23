# Supervised Binning Steps

Before doing a supervised binning, first run Step0_Eukfinder_long.sh to get classification by Eukfinder_long.
The centrifuge result in the tmps folder and the classified EUnk.fasta will be used for next step.

------------------------------------------------------------------------------
## Step 1. Parse centrifuge result:

source activate python36-generic
python3 Step1_Parsing_centrifuge_results.py

--------------------
INPUT FILE:(results from Step0_Eukfinder_long.sh)
The centrifuge result in the tmps folder

OUTPUT:
```sh
    Eukaryotic species with more than 10 contigs detected by Centrifuge:

                          species  centrifuge_count
    0  Blastocystis sp. subtype 4              3300
    1     Cyclospora cayetanensis                15
```


OUTPUT FILE:
Step1_parsed_centrifuge_results_eukLong.txt
------------------------------------------------------------------------------
## Step 2. Run Plast and Parse Plast result:

run Step2.1_run_Plast.sh
DB=/scratch5/db/Eukfinder/nt2021/nt.fasta

source activate python36-generic
python3 Step2.2_Parsing_Plast_results.py

--------------------
INPUT FILE:(results from Step2.1_run_Plast.sh)
Eukfinder_long.PLAST_nt.tsv


OUTPUT:
```sh
    Eukaryotic species with more than 10 contigs detected by Plast:

                       species  Plast_count
    Blastocystis sp. subtype 4         3046
          Blastocystis hominis           33


OUTPUT FILE:
Step2_parsed_Plast_Acc2tax_results.txt
------------------------------------------------------------------------------
## Step 3. Run Step3_Blast_mito.sh

BLASTDB=/scratch5/db/Eukfinder/Mitochondrial


OUTPUT FILE:
Eukfinder_long_BLAST4Mit.out
------------------------------------------------------------------------------

## Step 4. Binning

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

source activate python36-generic
python3 Step4.5_binning_results.tsv

------------------------------------------------------------------------------
## Step 5. Parse all results to generate recovered eukaryotic genomes.

source activate python36-generic
python3 Step5_Parsing_binning_resutls.py
