import os
from pynwb import load_namespaces, register_class
from pynwb.file import LabMetaData
from hdmf.utils import docval, call_docval_func, get_docval

name = 'ndx-mvdmlab-metadata'

spec_path = os.path.abspath(os.path.dirname(__file__))
ns_path = os.path.join(spec_path, 'spec', f'{name}.namespace.yaml')

# This ensures the namespace is loaded
load_namespaces(ns_path)

@register_class('OdorantInfoExtension', name)
class OdorantInfoExtension(LabMetaData):
    """
    Class for storing odorant information from MVDMlab experiments
    """
    __nwbfields__ = ('odorA', 'odorB', 'odorC', 'odorD', 'odorE', 'odorF', 'odorG')

    @docval(
        {'name': 'name', 'type': str, 'doc': 'name of this OdorantInfoExtension container'},
        {'name': 'odorA', 'type': str, 'doc': 'Identity of odor A', 'default': None},
        {'name': 'odorB', 'type': str, 'doc': 'Identity of odor B', 'default': None},
        {'name': 'odorC', 'type': str, 'doc': 'Identity of odor C', 'default': None},
        {'name': 'odorD', 'type': str, 'doc': 'Identity of odor D', 'default': None},
        {'name': 'odorE', 'type': str, 'doc': 'Identity of odor E', 'default': None},
        {'name': 'odorF', 'type': str, 'doc': 'Identity of odor F', 'default': None},
        {'name': 'odorG', 'type': str, 'doc': 'Identity of odor G', 'default': None}
    )
    def __init__(self, **kwargs):
        call_docval_func(super(OdorantInfoExtension, self).__init__, kwargs)
        self.odorA = kwargs.get('odorA')
        self.odorB = kwargs.get('odorB')
        self.odorC = kwargs.get('odorC')
        self.odorD = kwargs.get('odorD')
        self.odorE = kwargs.get('odorE')
        self.odorF = kwargs.get('odorF')
        self.odorG = kwargs.get('odorG')
