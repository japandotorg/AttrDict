"""
attrdict contains several mapping objects that allow access to their
keys as attributes.
"""

from typing import List

from attrdict.mapping import AttrMap
from attrdict.dictionary import AttrDict
from attrdict.default import AttrDefault
from attrdict.orderedattrdict import OrderedAttrDict, CounterAttrDict, DefaultAttrDict, Tree
from attrdict.ordereddict import OrderedDict


__all__: List[str] = [
    'AttrMap', 
    'AttrDict', 
    'AttrDefault', 
    'OrderedAttrDict', 
    'CounterAttrDict', 
    'DefaultAttrDict', 
    'Tree',
    'OrderedDict',
]
