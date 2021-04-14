# :coding: utf-8

import json

import pytest

import roman_numerals


with open("numerals.json", "r") as f:
    TEST_ROMAN_NUMERALS_LIST = (
        (int(k), v) for k,v in json.load(f).items()
    )


@pytest.mark.parametrize("value, numerals", TEST_ROMAN_NUMERALS_LIST)
def test_score(value, numerals):
    assert roman_numerals.convert(value) == numerals


@pytest.mark.parametrize("unsupported_value", [0, -1, 5001, 5002])
def test_outside_range(unsupported_value):
    with pytest.raises(NotImplementedError):
        roman_numerals.convert(unsupported_value)