# :coding: utf-8

import json

import pytest

import roman_numerals


with open("numerals.json", "r") as f:
    TEST_ROMAN_NUMERALS_LIST = (
        (k,v) for k,v in json.load(f).items()
    )


@pytest.mark.parametrize("value, numerals", TEST_ROMAN_NUMERALS_LIST)
def test_score(value, numerals):
    assert roman_numerals.convert(value) == numerals
