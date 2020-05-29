# Makes a heuristic file and then writes it to the current working directory

import os
import random

def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be valid format string')
    return template, outtype, annotation_classes

def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where

    allowed template fields - follow python string module:

    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """

    # Keys define the type of scan
    # Below extracts T1, BOLD, and DWI
    # Paths done in BIDS format

    t1w = create_key('sub-{subject}/anat/sub-{subject}_T1w')
    bold = create_key('sub-{subject}/func/sub-{subject}_task-images_run-{item:01d}_bold')
    dwi = create_key('sub-{subject}/dwi/sub-{subject}_dwi')
    info = {t1w: [], bold: [], dwi: []}

    for idx, s in enumerate(seqinfo):
        # s is a named tuple with fields equal to the names of the columns
        # that are found in the dicominfo.tsv file
        if (s.dim4 == 1) and ('mprage' in s.series_id):
            info[t1w].append(s.series_id) # assign if a single scan meets criteria
        if (s.dim4 == 196) and ('pace_moco' in s.series_id):
            info[bold].append(s.series_id) # append for each scan that meets criteria
        if (s.dim3 == 37) and ('diff_mddw' in s.series_description):
            info[dwi].append(s.series_id) # append for each scan that meets criteria
    return info