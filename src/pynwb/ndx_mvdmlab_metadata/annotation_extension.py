import os
from pynwb import load_namespaces, register_class
from pynwb.file import LabMetaData
from hdmf.utils import docval, call_docval_func, get_docval

name = 'ndx-mvdmlab-metadata'

spec_path = os.path.abspath(os.path.dirname(__file__))
ns_path = os.path.join(spec_path, 'spec', f'{name}.namespace.yaml')

# This ensures the namespace is loaded
load_namespaces(ns_path)

@register_class('ExperimenterAnnotationExtension', name)
class ExperimenterAnnotationExtension(LabMetaData):
    """
    Class for storing experimenter annotations about specific channels
    """
    # Define all possible annotation fields
    __nwbfields__ = (
        'imec0_shank0_SWR_channel', 'imec0_shank1_SWR_channel', 
        'imec0_shank2_SWR_channel', 'imec0_shank3_SWR_channel',
        'imec1_shank0_SWR_channel', 'imec1_shank1_SWR_channel', 
        'imec1_shank2_SWR_channel', 'imec1_shank3_SWR_channel',
        'imec0_best_SWR_channel', 'imec1_best_SWR_channel',
        'imec0_best_control_channel', 'imec1_best_control_channel'
    )

    @docval(
        {'name': 'name', 'type': str, 'doc': 'name of this ExperimenterAnnotationExtension container'},
        {'name': 'imec0_shank0_SWR_channel', 'type': str, 'doc': 'Channel on imec0 shank0 with best SWR activity', 'default': None},
        {'name': 'imec0_shank1_SWR_channel', 'type': str, 'doc': 'Channel on imec0 shank1 with best SWR activity', 'default': None},
        {'name': 'imec0_shank2_SWR_channel', 'type': str, 'doc': 'Channel on imec0 shank2 with best SWR activity', 'default': None},
        {'name': 'imec0_shank3_SWR_channel', 'type': str, 'doc': 'Channel on imec0 shank3 with best SWR activity', 'default': None},
        {'name': 'imec1_shank0_SWR_channel', 'type': str, 'doc': 'Channel on imec1 shank0 with best SWR activity', 'default': None},
        {'name': 'imec1_shank1_SWR_channel', 'type': str, 'doc': 'Channel on imec1 shank1 with best SWR activity', 'default': None},
        {'name': 'imec1_shank2_SWR_channel', 'type': str, 'doc': 'Channel on imec1 shank2 with best SWR activity', 'default': None},
        {'name': 'imec1_shank3_SWR_channel', 'type': str, 'doc': 'Channel on imec1 shank3 with best SWR activity', 'default': None},
        {'name': 'imec0_best_SWR_channel', 'type': str, 'doc': 'Best SWR channel on imec0', 'default': None},
        {'name': 'imec1_best_SWR_channel', 'type': str, 'doc': 'Best SWR channel on imec1', 'default': None},
        {'name': 'imec0_best_control_channel', 'type': str, 'doc': 'Best control channel on imec0', 'default': None},
        {'name': 'imec1_best_control_channel', 'type': str, 'doc': 'Best control channel on imec1', 'default': None}
    )
    def __init__(self, **kwargs):
        call_docval_func(super(ExperimenterAnnotationExtension, self).__init__, kwargs)
        
        # Set all fields
        for field in self.__nwbfields__:
            setattr(self, field, kwargs.get(field, None))
