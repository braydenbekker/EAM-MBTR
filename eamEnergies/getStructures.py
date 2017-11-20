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
    
Notes:
    lines with #pragma: no cover have been extensively unit tested through commandline tests and were exculded here
    as they could not be unit tested by pytest without parsing argv and adding values at run time.
'''
import shutil
import numpy as np
import os
import random
import sys

def GenEnumOut(structure, arg):
    '''
    Compute the struct_enum.out vasp file.

    Args:
        enum.x (fortran, enumlib): computes derivative superstructures of a system.
        struct_enum.in (vasp, INCAR): vasp input file for each lattice structure
    Returns:
        enum_'lattice'/'Binary or Ternary'/Struct_enum.out
    '''
    if(len(sys.argv)>1): arg = sys.argv 

    if(len(arg[1])>2): 
        for lattice in structure:
            os.chdir("enum_%s/%s/"%(lattice, arg[1]))

            input_file=('struct_enum.in')
        
            enum="./../../enum.x %s" %(input_file)
            os.system(enum)
            os.chdir("../../")
        return 1
    return 0 #pragma: no cover

def GenVaspFiles(structure, arg, test,  conc1="1211 7140 200", conc2="1 500"):
    '''
    Generate 7500 vasp files, 2500 from each chosen lattice type.

    Args:
        structure (np.array): array of chosen lattice types
        struct_enum.out (vasp. OUTCAR): precomputed vasp outcar for each lattice type
        system (argv): 2-4 space separated elements as command line args
    Returns:
        Structure_'system'/'fcc/, bcc/, hcp'/vasp.num where num=1-2500
    '''
    if(len(sys.argv)>1): arg = sys.argv

    elements = []
    system = ""
    directory="Structures_"
    for i in arg:
        elements.append(i) #get the selected elements from command line                                        
        if(len(i)==2): 
            directory=(directory + "%s"%(i))
            system = system + " " + i
    if(len(system)==6): systemType="Binary"
    elif(len(system)==9): systemType="Ternary"
    
    try:
        os.mkdir(directory)
        
    homedirectory = os.getcwd()
    workingdirectory = ("%s/%s"%(os.getcwd(), directory)) #file path to enumlib files             
    os.chdir(workingdirectory)


    for lattice in structure:
        directory_lattice="%s"%(lattice)
        os.mkdir(directory_lattice)
        os.chdir("./" + directory_lattice + "/")
        os.system(("cp %s/enum_%s/%s/struct_enum.out %s") 
                  %(homedirectory, lattice, systemType, os.getcwd()))
    
        makestructures="python %s/makeStr.py %s -species %s" %(homedirectory, conc1, system)
        os.system(makestructures)

        makestructures="python %s/makeStr.py %s -species %s" %(homedirectory, conc2, system)
        os.system(makestructures)

        os.system("rm struct_enum.out")
        os.chdir("../")

    return 1

def main():
    '''
    enumlib computes the derivative superstructures of a system. 
    getStructures.py has two principle classes: compute the struct_enum.out using enum.x,
    second, compute the derivative superstructures using the struct_enum.out for fcc, bcc, hcp.

    Args:
         struct_enum.in.'struct' (vasp POSCAR): binary, ternary, quaternary POSCAC file
         enum.x (fortran, enumlib): required code for creating struct_enum.out
         makeStr.py (Python, enumlib): edited from oririnal to allow for random sampling
         system (argv, 2-4): 2 to 4 element names, space separated (e.g. Al Ti) 

    Returns: 
         struct_enum.out (vasp OUTCAR): the outcar must contain >7140 
                       structures that is up to 12 atom cells for fcc
         Structure_'system'/fcc /bcc /hcp /vasp.'num' (vasp files): num=(1-2500), first 1-500 structures,
                       second 500-2500 sampled  randomly for 10-12 atom cells or more generally between 1211-7140  
    '''
    structure = np.array(["fcc","bcc","hcp"]) #the three desired crystal lattice types 
    if(len(sys.argv) > 1):
        ran =  GenEnumOut(structure, arg=[""]) #pragma: no cover

        if(ran == 0): GenVaspFiles(structure, arg=[""], test=False, conc1="100 200 5", conc2="1 5") #pragma: no cover
    return 0

main()
