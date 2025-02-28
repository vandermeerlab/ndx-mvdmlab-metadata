import os
from pynwb import load_namespaces, get_class

name = 'ndx-mvdmlab-metadata'

spec_path = os.path.abspath(os.path.dirname(__file__))
ns_path = os.path.join(spec_path, 'spec', f'{name}.namespace.yaml')

load_namespaces(ns_path)
LabMetaDataExtension = get_class('LabMetaDataExtension', name)
ProbeExtension = get_class('ProbeExtension', name)
OdorantInfoExtension = get_class('OdorantInfoExtension', name)
ExperimentalBlockExtension = get_class('ExperimentalBlockExtension', name)
ExperimenterAnnotationExtension = get_class('ExperimenterAnnotationExtension', name)