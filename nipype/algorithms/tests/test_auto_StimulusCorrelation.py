# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.algorithms.rapidart import StimulusCorrelation

def test_StimulusCorrelation_inputs():
    input_map = dict(concatenated_design=dict(mandatory=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    intensity_values=dict(mandatory=True,
    ),
    realignment_parameters=dict(mandatory=True,
    ),
    spm_mat_file=dict(mandatory=True,
    ),
    )
    inputs = StimulusCorrelation.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_StimulusCorrelation_outputs():
    output_map = dict(stimcorr_files=dict(),
    )
    outputs = StimulusCorrelation.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

