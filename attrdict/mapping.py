"""
An implementation of MutableAttr.
"""

from collections.abc import Mapping
from typing import Any, Type, Tuple, Sequence, Union, Iterable, List
from typing_extensions import Self

import six

from attrdict.mixins import MutableAttr


__all__: List[str] = ['AttrMap']


class AttrMap(MutableAttr):
    """
    An implementation of MutableAttr.
    """
    def __init__(
        self, 
        items: Any = None, 
        sequence_type: Type[Tuple[Any, ...]] = tuple
    ) -> None:
        super().__init__()
        
        if items is None:
            items = {}
        elif not isinstance(items, Mapping):
            items = dict(items)

        self._setattr('_sequence_type', sequence_type)
        self._setattr('_mapping', items)
        self._setattr('_allow_invalid_attributes', False)

    def _configuration(self) -> Union[Any, Sequence[Any]]:
        """
        The configuration for an attrmap instance.
        """
        return self._sequence_type

    def __getitem__(self, key: Any) -> Any:
        """
        Access a value associated with a key.
        """
        return self._mapping[key]

    def __setitem__(self, key: Any, value: Any) -> None:
        """
        Add a key-value pair to the instance.
        """
        self._mapping[key] = value

    def __delitem__(self, key: Any) -> None:
        """
        Delete a key-value pair
        """
        del self._mapping[key]

    def __len__(self) -> int:
        """
        Check the length of the mapping.
        """
        return len(self._mapping)

    def __iter__(self) -> Iterable:
        """
        Iterated through the keys.
        """
        return iter(self._mapping)

    def __repr__(self) -> str:
        """
        Return a string representation of the object.
        """
        # sequence type seems like more trouble than it is worth.
        # If people want full serialization, they can pickle, and in
        # 99% of cases, sequence_type won't change anyway
        return six.u("{name}({mapping})").format(
            name=self.__class__.__name__,
            mapping=repr(self._mapping)
        )

    def __getstate__(self) -> Union[Any, Sequence[Any]]:
        """
        Serialize the object.
        """
        return (
            self._mapping,
            self._sequence_type,
            self._allow_invalid_attributes
        )

    def __setstate__(self, state: Any) -> None:
        """
        Deserialize the object.
        """
        mapping, sequence_type, allow_invalid_attributes = state
        self._setattr('_mapping', mapping)
        self._setattr('_sequence_type', sequence_type)
        self._setattr('_allow_invalid_attributes', allow_invalid_attributes)

    @classmethod
    def _constructor(cls, mapping: Union[Any, Mapping[Any, Any]], configuration: Any) -> Self:
        """
        A standardized constructor.
        """
        return cls(mapping, sequence_type=configuration)
