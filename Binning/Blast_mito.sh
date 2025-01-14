#!/bin/bash
#$ -S /bin/bash
. /etc/profile
#$ -cwd
#$ -pe threaded 30
cd $PWD

query=Eukfinder_long.fasta

source activate blast
export BLASTDB=/scratch5/db/Eukfinder/Mitochondrial
DB=mito_blast_db
blastn -db $DB -query $query -out ${query::-6}_BLAST4Mit.out -num_threads 30 -outfmt "6 qseqid sseqid stitle evalue pident qcovhsp nident mismatch length slen qlen qstart qend sstart send staxids sscinames sskingdoms" -evalue 1E-5 -max_hsps 1
conda deactivate

