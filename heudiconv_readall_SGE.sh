#!/bin/bash
#$ -V
#$ -cwd
#$ -S /bin/bash
#$ -N heudiconv_readfiles
#$ -o logs/subject_$TASK_ID.out
#$ -e logs/subject_$TASK_ID.out
#$ -m be -M jacob.taylor.fisher@gmail.com
#$ -q omni
#$ -pe mpi 36
#$ -P quanah
#$ -t 1-30

heudiconv -d dicomdir/*{subject}/* -f code/convertall.py -s $(printf %02d $SGE_TASK_ID)  --minmeta -c none -o heudiconv_temp --overwrite