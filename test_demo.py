import pytest


def fun(x):
    return x + 5


def test_01():
    assert fun(3) == 8


def test_02():
    assert fun(4) == 9
