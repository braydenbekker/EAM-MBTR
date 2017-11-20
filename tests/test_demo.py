"""Tests the mathematical functions defined in eamEnergies/getStructures.py
"""

import pytest

def test_GenEnumOut():
    """Tests the squaring function"""
    from eamEnergies.getStructures import GenEnumOut, GenVaspFiles

    lattice = ["fcc","bcc","hcp"]
    
    arg = ["filename", "Binary"]
    assert 1 == GenEnumOut(lattice, arg)
    
    arg = ["filename", "Ternary"]
    assert 1 == GenEnumOut(lattice, arg)

    arg = ["filename", "Al", "Ti"]
    assert 1 == GenVaspFiles(lattice, arg, test=True, conc1="100 200 5", conc2="1 5")

    arg = ["filename", "Al", "Co", "Ni"]
    assert 1 == GenVaspFiles(lattice, arg, test=True, conc1="100 200 5", conc2="1 5")
    return

