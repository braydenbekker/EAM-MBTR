"""Tests the mathematical functions defined in demo/trail.py
"""

import pytest

def test_sqaure():
    """Tests the squaring function"""

    from eamEnergies.trial import square

    assert 4 == square(2)
