'''
Author Brayden Bekker

getStructures.py uses the enumlib code created by the MSG group at BYU, https://github.com/msg-byu/enumlib. enumlib is 
designed to compute the derivative superstructures for a system of elements and a given lattice. 

Input:
    - path to makeStr.py and enum.x from enumlib.
    - precomputed struct_enum.out files for FCC, BCC, and HCP through 7140 structures.

Output:
    - a directory (e.g. Structures_AlTi) whith sub directories, fcc, bcc, hcp
    - each subdirectory contains 2500 vasp POSCAR files with atom concentrations and positions.
    (the first 500 derivative superstructures and 2000 additional structures from higher atom cells 10-12)
    
File Structure:
cd path/to/program/files/
ls
Structures/ struct_enum.in.fcc, struct_enum.in.bcc, struct_enum.in.hcp
enum_(fcc,bcc,hcp)/struct_enum.out
makeStr.py
./enum.x
'''
import shutil
import numpy as np
import os
import random
import sys

def square(x):
    """Finds the square of the input.
    
    Args:
        x (float): The number to be squared.

    Returns:
        x2 (float): The squared number.
    """

    return x**2
