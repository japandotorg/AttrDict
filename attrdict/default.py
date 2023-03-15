"""
A subclass of MutableAttr that has defaultdict support.
"""
from collections.abc import Mapping
from typing import Any, Type, Tuple, Sequence, Union, Iterable, List
from typing_extensions import Self

import six

from attrdict.mixins import MutableAttr


__all__: List[str] = ["AttrDefault"]


class AttrDefault(MutableAttr):
    """
    An implementation of MutableAttr with defaultdict support
    """

    def __init__(
        self, 
        default_factory: Any = None, 
        items: Any = None, 
        sequence_type: Type[Tuple[Any, ...]] = tuple, 
        pass_key: bool = False,
    ) -> None:
        super().__init__()
        
        if items is None:
            items = {}
        elif not isinstance(items, Mapping):
            items = dict(items)

        self._setattr("_default_factory", default_factory)
        self._setattr("_mapping", items)
        self._setattr("_sequence_type", sequence_type)
        self._setattr("_pass_key", pass_key)
        self._setattr("_allow_invalid_attributes", False)

    def _configuration(self) -> Union[Tuple, Any, Sequence[Any], str, six.binary_type]:
        """
        The configuration for a AttrDefault instance
        """
        return self._sequence_type, self._default_factory, self._pass_key

    def __getitem__(self, key: Any) -> Union[Any, KeyError]:
        """
        Access a value associated with a key.

        Note: values returned will not be wrapped, even if recursive
        is True.
        """
        if key in self._mapping:
            return self._mapping[key]
        elif self._default_factory is not None:
            return self.__missing__(key)

        raise KeyError(key)

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

    def __missing__(self, key: Any) -> Any:
        """
        Add a missing element.
        """
        if self._pass_key:
            self[key] = value = self._default_factory(key)
        else:
            self[key] = value = self._default_factory()

        return value

    def __repr__(self) -> str:
        """
        Return a string representation of the object.
        """
        return six.u("{name}({default_factory}, {pass_key}, {mapping})").format(
            name=self.__class__.__name__,
            default_factory=repr(self._default_factory),
            pass_key=repr(self._pass_key),
            mapping=repr(self._mapping),
        )

    def __getstate__(self) -> Union[Any, Sequence[Any]]:
        """
        Serialize the object.
        """
        return (
            self._default_factory,
            self._mapping,
            self._sequence_type,
            self._pass_key,
            self._allow_invalid_attributes,
        )

    def __setstate__(self, state: Any) -> None:
        """
        Deserialize the object.
        """
        (
            default_factory,
            mapping,
            sequence_type,
            pass_key,
            allow_invalid_attributes,
        ) = state

        self._setattr("_default_factory", default_factory)
        self._setattr("_mapping", mapping)
        self._setattr("_sequence_type", sequence_type)
        self._setattr("_pass_key", pass_key)
        self._setattr("_allow_invalid_attributes", allow_invalid_attributes)

    @classmethod
    def _constructor(cls, mapping: Union[Any, Mapping[Any, Any]], configuration: Any) -> Self:
        """
        A standardized constructor.
        """
        sequence_type, default_factory, pass_key = configuration
        return cls(
            default_factory, mapping, sequence_type=sequence_type, pass_key=pass_key
        )
