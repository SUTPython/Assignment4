from canister import Canister
import pytest


def test_init():
    c = Canister()
    assert c.capacity == 12
    assert c.volume == 0

    c2 = Canister(5)
    assert c2.capacity == 5

    with pytest.raises(ValueError):
        Canister(-1)
    with pytest.raises(ValueError):
        Canister("a")


def test_str():
    c = Canister()
    assert str(c) == ""
    c.refill(1)
    assert str(c) == "🥤"
    c.refill(2)
    assert str(c) == "🥤🥤🥤"


def test_refill():
    c = Canister(5)
    c.refill(2)
    assert c.volume == 2
    c.refill(3)
    assert c.volume == 5
    with pytest.raises(ValueError):
        c.refill(1)


def test_drink():
    c = Canister(5)
    c.refill(4)
    c.drink(2)
    assert c.volume == 2
    c.drink(2)
    assert c.volume == 0
    with pytest.raises(ValueError):
        c.drink(1)
