# Eukfinder
A bioinformatics tool designed to enable rapid recovery of high-quality draft genomes of microbial eukaryotes from various environmental metagenomic samples.

- reference-independent and cultivation-free
- separate reads or contigs into five groups: Bacteria, Archaeal, Eukaryotic, Viral, and Unknown. 
- generate a fasta file with Euk and unknown contigs for binning


## Overview
![Graphical_abstract](https://user-images.githubusercontent.com/39600837/215847526-31479e80-fa55-48b0-a56f-643d166db5e5.png)

## Publication/Citation
Currently under development


## Requirements


## Installation 

 
## Download of reference databases 

 Users can flexibly customize the reference data (see here)
 
 Default reference databases can be downloaded from [Eukfinder Databases](https://perun.biochem.dal.ca/Metagenomics-Scavenger/)


<!-- USAGE EXAMPLES -->
## Usage

**Eukfinder read_prep**
usage: Eukfinder read_prep [-h] --r1 R1 --r2 R2 -n THREADS -i ILLUMINA_CLIP
                           --hcrop HCROP -l LEADING_TRIM -t TRAIL_TRIM --wsize
                           WSIZE --qscore QSCORE --mlen MLEN --hg HG -o
                           OUT_NAME --cdb CDB

optional arguments:
  -h, --help            show this help message and exit

Required arguments:
  Description

  --r1 R1, --reads-r1 R1    left reads
  
  --r2 R2, --reads-r2 R2    right reads
  
  -n THREADS, --threads THREADS     number of threads
                        
  -i ILLUMINA_CLIP, --illumina-clip ILLUMINA_CLIP     adaptor file
                        
  --hcrop HCROP, --head-crop HCROP    head trim
                        
  -l LEADING_TRIM, --leading-trim LEADING_TRIM    leading trim
                        
  -t TRAIL_TRIM, --trail-trim TRAIL_TRIM    trail trim
                        
  --wsize WSIZE, --window-size WSIZE    sliding window size
                        
  --qscore QSCORE, --quality-score QSCORE     quality score for trimming
                        
  --mlen MLEN, --min-length MLEN    minimum length
                        
  --hg HG, --host-genome HG     host genome to get map out
                        
  -o OUT_NAME, --out_name OUT_NAME    out name
                        
  --cdb CDB, --centrifuge-database CDB    path to centrifuge database
  
  
<!-- ROADMAP -->
## Roadmap

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments


<p align="right">(<a href="#readme-top">back to top</a>)</p>
