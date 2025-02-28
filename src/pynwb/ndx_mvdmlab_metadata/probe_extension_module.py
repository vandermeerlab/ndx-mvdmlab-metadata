import os
from pynwb import load_namespaces, register_class
from pynwb.file import LabMetaData
from hdmf.utils import docval, call_docval_func, get_docval

name = 'ndx-mvdmlab-metadata'

spec_path = os.path.abspath(os.path.dirname(__file__))
ns_path = os.path.join(spec_path, 'spec', f'{name}.namespace.yaml')

# This ensures the namespace is loaded
load_namespaces(ns_path)

@register_class('ProbeExtension', name)
class ProbeExtension(LabMetaData):
    """
    Class for storing probe information from MVDMlab experiments
    """
    __nwbfields__ = (
        'ID', 'hemisphere', 'Depth', 'AP', 'ML', 
        'roll', 'pitch', 'yaw', 'area'
    )

    @docval(
        {'name': 'name', 'type': str, 'doc': 'name of this ProbeExtension container'},
        {'name': 'ID', 'type': str, 'doc': 'Probe identifier', 'default': None},
        {'name': 'hemisphere', 'type': str, 'doc': 'Brain hemisphere where probe was placed', 'default': None},
        {'name': 'Depth', 'type': float, 'doc': 'Depth of probe insertion in mm', 'default': None},
        {'name': 'AP', 'type': float, 'doc': 'Anterior-posterior coordinates', 'default': None},
        {'name': 'ML', 'type': float, 'doc': 'Medial-lateral coordinates', 'default': None},
        {'name': 'roll', 'type': float, 'doc': 'Roll angle of probe', 'default': None},
        {'name': 'pitch', 'type': float, 'doc': 'Pitch angle of probe', 'default': None},
        {'name': 'yaw', 'type': float, 'doc': 'Yaw angle of probe', 'default': None},
        {'name': 'area', 'type': str, 'doc': 'Brain area targeted', 'default': None}
    )
    def __init__(self, **kwargs):
        call_docval_func(super(ProbeExtension, self).__init__, kwargs)
        self.ID = kwargs.get('ID')
        self.hemisphere = kwargs.get('hemisphere')
        self.Depth = kwargs.get('Depth')
        self.AP = kwargs.get('AP')
        self.ML = kwargs.get('ML')
        self.roll = kwargs.get('roll')
        self.pitch = kwargs.get('pitch')
        self.yaw = kwargs.get('yaw')
        self.area = kwargs.get('area')
