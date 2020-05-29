singularity run --cleanenv collab_files/my_images/fmriprep-latest.simg \
    collab_files/bids_nii collab_files/preproc \
    participant \
    --participant-label 20 --nthreads 16 --fs-no-reconall --fd-spike-threshold .5 --use-aroma -w collab_files/preproc/fmriprep_work \