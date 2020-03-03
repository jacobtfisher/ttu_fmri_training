import os
def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes
def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where
    allowed template fields - follow python string module:
    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """
    t1w = create_key('sub-{subject}/{session}/anat/sub-{subject}_{session}_run-00{item:01d}_T1w')
    func_rest = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-rest_run-00{item:01d}_bold')
    func_rest_matrix96 =  create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-rest_run-00{item:01d}_bold')
    func_rest_matrix96_sbref =  create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-rest_run-00{item:01d}_sbref')
    fmap_mag =  create_key('sub-{subject}/{session}/fmap/sub-{subject}_{session}_magnitude')
    fmap_phase = create_key('sub-{subject}/{session}/fmap/sub-{subject}_{session}_phasediff')
    dwi = create_key('sub-{subject}/{session}/dwi/sub-{subject}_{session}_run-00{item:01d}_dwi')

    info = {t1w: [], func_rest: [],    func_rest_matrix96: [], func_rest_matrix96_sbref: [], fmap_mag: [], fmap_phase: [], dwi: []}
    
    for idx, s in enumerate(seqinfo):
        if (s.dim1 == 320) and (s.dim2 == 320) and ('t1_fl2d_tra' in s.protocol_name):
            info[t1w].append(s.series_id)
        if (s.dim1 == 128) and (s.dim2 == 128) and ('Resting State fMRI MBEPI' in s.protocol_name):
            info[func_rest].append(s.series_id)
        if (s.dim1 == 96) and (s.dim4 == 518) and ('Resting State fMRI MBEPI_matrix96_BW2004' in s.protocol_name):
            info[func_rest_matrix96].append(s.series_id)
        if (s.dim1 == 96) and (s.dim4 == 1) and ('Resting State fMRI MBEPI_matrix96_BW2004' in s.protocol_name):
            info[func_rest_matrix96_sbref].append(s.series_id)
        if (s.dim3 == 136) and (s.dim4 == 1) and ('gre_field_mapping' in s.protocol_name):
            info[fmap_mag] = [s.series_id]
        if (s.dim3 == 68) and (s.dim4 == 1) and ('gre_field_mapping' in s.protocol_name):
            info[fmap_phase] = [s.series_id]
        if (s.dim2 == 128) and (s.dim4 == 64):
            info[dwi].append(s.series_id)
    return info

