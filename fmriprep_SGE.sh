#!/bin/bash
#$ -V
#$ -cwd
#$ -S /bin/bash
#$ -N fmriprep
#$ -o logs/fmriprep/subject_$TASK_ID.out
#$ -e logs/fmriprep/subject_$TASK_ID.out
#$ -m be -M jacob.taylor.fisher@gmail.com
#$ -q omni
#$ -pe mpi 36
#$ -P quanah
#$ -t 20

module load singularity 

export SINGULARITYENV_FS_LICENSE=$HOME/.licenses/freesurfer/license.txt

singularity run --cleanenv my_images/fmriprep-latest.simg bids_nii preproc participant --participant-label $(printf %02d $SGE_TASK_ID) --nthreads 36 --fs-no-reconall --fd-spike-threshold .5 --use-aroma -w preproc/fmriprep_work