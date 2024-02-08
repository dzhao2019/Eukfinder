# Eukfinder
A bioinformatics tool designed to enable rapid recovery of high-quality draft genomes of microbial eukaryotes from various environmental metagenomic samples.

- reference-independent and cultivation-free
- separate reads or contigs into five groups: Bacteria, Archaeal, Eukaryotic, Viral, and Unknown. 
- generate a fasta file with Euk and unknown contigs for binning


## Overview
Schematic representation of Eukfinder workflows. Eukfinder is a taxonomic classification-based bioinformatics approach to retrieve microbial eukaryotic nuclear and mitochondrial genomes from WGS metagenomic sequencing data. Eukfinder has two different workflows based on the input files, (a) Eukfinder_short using Illumina short reads, it first classifies Illumina reads into 5 distinct taxonomic categories (Archaeal, Bacterial, Viral, Eukaryotic, and Unknown), after assembling the Eukaryotic and Unknown reads together, second round of classification and supervised binning, it will output Eukaryotic nuclear and mitochondrial genomes, and (b) Eukfinder_long using MAG assembled contigs or long-read sequencing data generated by Nanopore or Pacbio platforms. It goes through one round of classification to select Eukaryotic and Unknown contigs, and after supervised binning generates Eukaryotic nuclear and mitochondrial genomes.
![Graphical_abstract](https://github.com/dzhao2019/Eukfinder_test/assets/39600837/907fd6e9-7833-41d3-a062-02fff2cb4601)


## Requirements
Python >= 3.7

ete3,numpy, pandas, joblib, pyqt, spades, seqkit, trimmomatic, bowtie2, centrifuge, acc2tax, plast


## Installation 

A step-by-step tutorial on installation.

Note: We are working to making Eukfinder available on Bioconda, so that this tutorial may be frequently updated.

### 1. Clone this repository

```sh
git clone https://github.com/RogerLab/Eukfinder.git
```

<br>

### 2. Create a conda environment for Eukfinder

Please install [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html) first.


```sh
conda env create -f eukfindertest.yml

# activate it
source activate eukfindertest
```

<br>

### 3. Install other dependencies

(Required) Install PLAST <br>

```sh
wget https://github.com/PLAST-software/plast-library/releases/download/v2.3.2/plastbinary_linux_v2.3.2.tar.gz
tar -zxf plastbinary_linux_v2.3.2.tar.gz
export PATH=/path/to/plastbinary_linux_v2.3.2/bin:$PATH
```
(Required) Install `acc2tax` <br>
https://github.com/richardmleggett/acc2tax

<br>
(Required for supervised binning) Install MyCC <br>
https://sourceforge.net/projects/sb2nhri/files/MyCC/

<br>

### 4. Download or build databases
 
  Default reference databases can be downloaded from [Eukfinder Databases](https://perun.biochem.dal.ca/Metagenomics-Scavenger/)
- Plast Database
- Centrifuge Database
- acc2tax Database

 Users can flexibly customize the reference data (see [here](https://github.com/dzhao2019/eukfindertest/wiki/Build-a-customized-reference-database))
 

<!-- USAGE EXAMPLES -->
## Usage
See [Wiki](https://github.com/dzhao2019/eukfindertest/wiki) for detailed description

**Eukfinder read_prep**
Run Trimmomatic to remove low-quality reads, and adaptors
Run Bowtie2 to remove host reads
Run Centrifuge for the first round of classification

    Eukfinder read_prep [-h] --r1 R1 --r2 R2 -n THREADS -i ILLUMINA_CLIP
                               --hcrop HCROP -l LEADING_TRIM -t TRAIL_TRIM --wsize
                               WSIZE --qscore QSCORE --mlen MLEN --hg HG -o
                               OUT_NAME --cdb CDB

  
**Eukfinder short_seqs**

    Eukfinder short_seqs [-h] --r1 R1 --r2 R2 --un UN -o OUT_NAME -n
                            NUMBER_OF_THREADS -z NUMBER_OF_CHUNKS -t
                            TAXONOMY_UPDATE -p PLAST_DATABASE -m PLAST_ID_MAP
                            [-p2 ANCILLARY_PLAST_DATABASE]
                            [-m2 ANCILLARY_PLAST_ID_MAP]
                            [--force-pdb FORCE_PDB] -a ACC2TAX_DATABASE --cdb
                            CDB -e E_VALUE --pid PID --cov COV --max_m MAX_M
                            --mhlen MHLEN --pclass PCLASS --uclass UCLASS


**Eukfinder long_seqs**

    Eukfinder long_seqs [-h] -l LONG_SEQS -o OUT_NAME --mhlen MHLEN --cdb
                           CDB -n NUMBER_OF_THREADS -z NUMBER_OF_CHUNKS -t
                           TAXONOMY_UPDATE -p PLAST_DATABASE -m PLAST_ID_MAP
                           -a ACC2TAX_DATABASE -e E_VALUE --pid PID --cov COV



<!-- CONTRIBUTING -->
## Contributing

Contributions are what makes the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<br>
## Publication/Citation
Zhao, D., Salas-Leiva, D.E., Williams, S.K., Dunn, K.A. and Roger, A.J., 2023. Eukfinder: a pipeline to retrieve microbial eukaryote genomes from metagenomic sequencing data. bioRxiv, pp.2023-12.

<br>
<!-- CONTACT -->
## Contact
d.zhao@dal.ca

ds2000@cam.ac.uk

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments


<p align="right">(<a href="#readme-top">back to top</a>)</p>
