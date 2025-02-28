import os
from pynwb.spec import NWBNamespaceBuilder, NWBGroupSpec, NWBAttributeSpec, export_spec


def main():
    ns_builder = NWBNamespaceBuilder(
        doc='type for storing metadata for MvdMLab',
        name='ndx-mvdmlab-metadata',
        version='0.1.0',
        author=['Manish Mohapatra'],
        contact=['manishofyore@gmail.com']
    )

    ns_builder.include_type('LabMetaData', namespace='core')
    ns_builder.include_type('DynamicTable', namespace='core')

    # Create LabMetaDataExtension
    LabMetaDataExtension = NWBGroupSpec(
        doc='type for storing MVDMlab metadata',
        neurodata_type_def='LabMetaDataExtension',
        neurodata_type_inc='LabMetaData',
        attributes=[
            NWBAttributeSpec(
                name='probe1_ID',
                doc='ID of probe 1',
                dtype='text',
                required=False
            ),
            NWBAttributeSpec(
                name='probe2_ID',
                doc='ID of probe 2',
                dtype='text',
                required=False
            ),
        ],
        groups=[
            NWBGroupSpec(
                name='probe1',
                neurodata_type_inc='ProbeExtension',
                doc='information about probe 1'
            ),
            NWBGroupSpec(
                name='probe2',
                neurodata_type_inc='ProbeExtension',
                doc='information about probe 2'
            ),
            NWBGroupSpec(
                name='odorant_info',
                neurodata_type_inc='OdorantInfoExtension',
                doc='information about odorants used'
            ),
            NWBGroupSpec(
                name='block_info',
                neurodata_type_inc='ExperimentalBlockExtension',
                doc='information about experimental blocks'
            ),
            NWBGroupSpec(
                name='channel_annotations',
                neurodata_type_inc='ExperimenterAnnotationExtension',
                doc='annotations about specific channels'
            ),
        ]
    )

    # Create ProbeExtension
    probe_attributes = [
        NWBAttributeSpec(name='ID', doc='Probe identifier', dtype='text', required=False),
        NWBAttributeSpec(name='hemisphere', doc='Brain hemisphere where probe was placed', dtype='text', required=False),
        NWBAttributeSpec(name='Depth', doc='Depth of probe insertion in mm', dtype='float', required=False),
        NWBAttributeSpec(name='AP', doc='Anterior-posterior coordinates', dtype='float', required=False),
        NWBAttributeSpec(name='ML', doc='Medial-lateral coordinates', dtype='float', required=False),
        NWBAttributeSpec(name='roll', doc='Roll angle of probe', dtype='float', required=False),
        NWBAttributeSpec(name='pitch', doc='Pitch angle of probe', dtype='float', required=False),
        NWBAttributeSpec(name='yaw', doc='Yaw angle of probe', dtype='float', required=False),
        NWBAttributeSpec(name='area', doc='Brain area targeted', dtype='text', required=False),
    ]
    
    ProbeExtension = NWBGroupSpec(
        doc='type for storing probe information',
        neurodata_type_def='ProbeExtension',
        neurodata_type_inc='LabMetaData',
        attributes=probe_attributes
    )

    # Create OdorantInfoExtension
    odor_attributes = []
    for odor in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        odor_attributes.append(
            NWBAttributeSpec(
                name=f'odor{odor}',
                doc=f'Identity of odor {odor}',
                dtype='text',
                required=False
            )
        )
    
    OdorantInfoExtension = NWBGroupSpec(
        doc='type for storing odorant information',
        neurodata_type_def='OdorantInfoExtension',
        neurodata_type_inc='LabMetaData',
        attributes=odor_attributes
    )

    # Create ExperimentalBlockExtension
    block_attributes = []
    for block in [1, 2, 3]:
        block_attributes.append(
            NWBAttributeSpec(
                name=f'block{block}_type',
                doc=f'Type of block {block}',
                dtype='text',
                required=False
            )
        )
    
    ExperimentalBlockExtension = NWBGroupSpec(
        doc='type for storing experimental block information',
        neurodata_type_def='ExperimentalBlockExtension',
        neurodata_type_inc='LabMetaData',
        attributes=block_attributes
    )

    # Create ExperimenterAnnotationExtension
    annotation_attributes = []
    
    # Add attributes for SWR and control channels
    for imec in [0, 1]:
        for shank in [0, 1, 2, 3]:
            annotation_attributes.append(
                NWBAttributeSpec(
                    name=f'imec{imec}_shank{shank}_SWR_channel',
                    doc=f'Channel on imec{imec} shank{shank} with best SWR activity',
                    dtype='text',
                    required=False
                )
            )
        
        annotation_attributes.append(
            NWBAttributeSpec(
                name=f'imec{imec}_best_SWR_channel',
                doc=f'Best SWR channel on imec{imec}',
                dtype='text',
                required=False
            )
        )
        
        annotation_attributes.append(
            NWBAttributeSpec(
                name=f'imec{imec}_best_control_channel',
                doc=f'Best control channel on imec{imec}',
                dtype='text',
                required=False
            )
        )
    
    ExperimenterAnnotationExtension = NWBGroupSpec(
        doc='type for storing experimenter annotations about specific channels',
        neurodata_type_def='ExperimenterAnnotationExtension',
        neurodata_type_inc='LabMetaData',
        attributes=annotation_attributes
    )

    # Export the extension to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    print(output_dir)
    export_spec(ns_builder, [LabMetaDataExtension, ProbeExtension, OdorantInfoExtension, 
                             ExperimentalBlockExtension, ExperimenterAnnotationExtension], output_dir)


if __name__ == "__main__":
    main()
