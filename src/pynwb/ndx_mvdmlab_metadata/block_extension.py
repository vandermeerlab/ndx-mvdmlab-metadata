import os
from pynwb import load_namespaces, register_class
from pynwb.file import LabMetaData
from hdmf.utils import docval, call_docval_func, get_docval

name = 'ndx-mvdmlab-metadata'

spec_path = os.path.abspath(os.path.dirname(__file__))
ns_path = os.path.join(spec_path, 'spec', f'{name}.namespace.yaml')

# This ensures the namespace is loaded
load_namespaces(ns_path)

@register_class('ExperimentalBlockExtension', name)
class ExperimentalBlockExtension(LabMetaData):
    """
    Class for storing experimental block information from MVDMlab experiments
    """
    __nwbfields__ = ('block1_type', 'block2_type', 'block3_type')

    @docval(
        {'name': 'name', 'type': str, 'doc': 'name of this ExperimentalBlockExtension container'},
        {'name': 'block1_type', 'type': str, 'doc': 'Type of block 1', 'default': None},
        {'name': 'block2_type', 'type': str, 'doc': 'Type of block 2', 'default': None},
        {'name': 'block3_type', 'type': str, 'doc': 'Type of block 3', 'default': None}
    )
    def __init__(self, **kwargs):
        call_docval_func(super(ExperimentalBlockExtension, self).__init__, kwargs)
        self.block1_type = kwargs.get('block1_type')
        self.block2_type = kwargs.get('block2_type')
        self.block3_type = kwargs.get('block3_type')
