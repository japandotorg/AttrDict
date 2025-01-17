"""
A dict that implements MutableAttr.
"""

from collections.abc import Mapping
from typing import Any, Sequence, Union, List
from typing_extensions import Self

from attrdict.mixins import MutableAttr

import six


__all__: List[str] = ['AttrDict']


class AttrDict(dict, MutableAttr):
    """
    A dict that implements MutableAttr.
    """
    def __init__(self, *args: Any, **kwargs: Any):
        super(AttrDict, self).__init__(*args, **kwargs)

        self._setattr('_sequence_type', tuple)
        self._setattr('_allow_invalid_attributes', False)

    def _configuration(self) -> Union[Any, Sequence[Any]]:
        """
        The configuration for an attrmap instance.
        """
        return self._sequence_type

    def __getstate__(self) -> Any:
        """
        Serialize the object.
        """
        return (
            self.copy(),
            self._sequence_type,
            self._allow_invalid_attributes
        )

    def __setstate__(self, state: Any) -> None:
        """
        Deserialize the object.
        """
        mapping, sequence_type, allow_invalid_attributes = state
        self.update(mapping)
        self._setattr('_sequence_type', sequence_type)
        self._setattr('_allow_invalid_attributes', allow_invalid_attributes)

    def __repr__(self) -> str:
        return six.u('{name}({contents})').format(
            name=self.__class__.__name__,
            contents=super(AttrDict, self).__repr__()
        )

    @classmethod
    def _constructor(cls, mapping: Union[Any, Mapping[Any, Any]], configuration: Any) -> Self:
        """
        A standardized constructor.
        """
        attr: Self = cls(mapping)
        attr._setattr('_sequence_type', configuration)

        return attr
