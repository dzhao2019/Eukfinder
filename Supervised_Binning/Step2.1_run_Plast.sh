#!/bin/bash
#$ -S /bin/bash
. /etc/profile
#$ -cwd
#$ -pe threaded 48
cd $PWD
source activate eukfinder
query=Eukfinder_long.fasta
# Run plast
DB=/scratch5/db/Eukfinder/nt2021/nt.fasta
plast -e 1E-5 -max-hit-per-query 1 -outfmt 1 -a 48 -p plastn -i $query -d $DB -force-query-order 1000 -o ${query::-6}.PLAST_nt.tsv

conda deactivate
