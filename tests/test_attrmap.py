"""
Tests for the AttrMap class.
"""
from nose.tools import assert_equals


def test_repr():
    """
    repr(AttrMap)
    """
    from attrdict.mapping import AttrMap

    assert_equals(repr(AttrMap()), "AttrMap({})")
    assert_equals(repr(AttrMap({"foo": "bar"})), "AttrMap({'foo': 'bar'})")
    assert_equals(repr(AttrMap({1: {"foo": "bar"}})), "AttrMap({1: {'foo': 'bar'}})")
    assert_equals(
        repr(AttrMap({1: AttrMap({"foo": "bar"})})),
        "AttrMap({1: AttrMap({'foo': 'bar'})})",
    )


def test_repr_subclass():
    """
    repr(AttrMap)
    """
    from attrdict.mapping import AttrMap

    class MySubClass(AttrMap):
        pass

    assert_equals(repr(MySubClass()), "MySubClass({})")
    assert_equals(repr(MySubClass({"foo": "bar"})), "MySubClass({'foo': 'bar'})")
    assert_equals(
        repr(MySubClass({1: {"foo": "bar"}})), "MySubClass({1: {'foo': 'bar'}})"
    )
    assert_equals(
        repr(MySubClass({1: MySubClass({"foo": "bar"})})),
        "MySubClass({1: MySubClass({'foo': 'bar'})})",
    )
