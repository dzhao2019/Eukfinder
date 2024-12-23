#!/bin/bash
#$ -S /bin/bash
. /etc/profile
#$ -cwd
#$ -pe threaded 20
cd $PWD
source activate eukfinder


# path to the eukfinder script
Eukfinder=/misc/scratch3/Eukfinder/eukfinder.py

# path to databases
plastdb=/scratch3/Eukfinder/DB/PLAST_DB/PlastDB_Jun2020.fasta
plastmap=/misc/scratch3/Eukfinder/DB/PLAST_DB/PlastDB_Jun2020_map.txt
centrifuge=/scratch3/Eukfinder/DB/Centrifuge_DB/Centrifuge_NewDB_Sept2020
acc2tax=/scratch3/Eukfinder/DB/Acc2tax/

input=ERR321632_scaffolds_1000.fasta
prefix=ERR321632_scaffolds_1000_Eukfinder_long

python $Eukfinder long_seqs -l $input -n 20 -z 3 -t False -p $plastdb -m $plastmap -a $acc2tax \
                       -e 0.01 --pid 80 --cov 30 -o $prefix --cdb $centrifuge --mhlen 40

conda deactivate
