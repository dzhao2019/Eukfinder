#!/bin/bash
#$ -S /bin/bash
. /etc/profile
#$ -cwd
#$ -pe threaded 10
cd $PWD

input=Eukfinder_long.fasta

source activate maxbin2
# Run maxbin2
echo "======== Run maxbin2 ========"
run_MaxBin.pl -contig $input -abund Eukfinder_long_EUnk.depth.txt -out maxbin2_binning -thread 10


source activate metabat2
# Run metabat2
echo "======== Run metabat2 ========"
metabat2 -i $input -o metabat2_binning -m 1500 -t 10  --unbinned -a Eukfinder_long_EUnk.depth.txt
mkdir Binning_results
mv maxbin2_* Binning_results
mv metabat2_* Binning_results

conda deactivate
