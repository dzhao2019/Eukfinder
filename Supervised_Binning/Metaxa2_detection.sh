#!/bin/bash
#$ -S /bin/bash
. /etc/profile
#$ -cwd
#$ -pe threaded 20
cd $PWD
mkdir Metaxa2_results
echo "==ERR321632_Eukfinder_long.fasta begins=="
metaxa2 --cpu 20 -g SSU -i Eukfinder_long.fasta -o Eukfinder_long_metaxa2_SSU
date
metaxa2 --cpu 20 -g LSU -i Eukfinder_long.fasta -o Eukfinder_long_metaxa2_LSU
date
echo "==ERR321632_Eukfinder_long.fasta finished=="
find . -type f -size 0 -delete
mv *_metaxa2_* Metaxa2_results
