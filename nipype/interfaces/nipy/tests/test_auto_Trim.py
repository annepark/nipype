# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.nipy.preprocess import Trim
def test_Trim_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    out_file=dict(),
    begin_index=dict(usedefault=True,
    ),
    end_index=dict(usedefault=True,
    ),
    in_file=dict(mandatory=True,
    ),
    suffix=dict(usedefault=True,
    ),
    )
    inputs = Trim.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_Trim_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = Trim.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value