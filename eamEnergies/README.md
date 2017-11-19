## getStructures.py

#### configuration
For file size purposes on github the struct_enum.in and getStructures.py have 
been modified to produce minimal output as follows:

(line 9: 1 4) will only produce an OUTCAR up to 4 atom cell size this must be changed for
larger computations in each INCAR
 
fcc

bulk
0.50000000     0.50000000      0.0000000        # a1 parent lattice vector

0.50000000      0.0000000     0.50000000        # a2 parent lattice vector

0.0000000     0.50000000     0.50000000        # a3 parent lattice vector
 
 2 -nary case
 
 1 # Number of points in the multilattice
 
 0.0000000      0.0000000      0.0000000    0/1   # d01 d-vector
 
 1 4   # Starting and ending cell sizes for search 

0.10000000E-06 # Epsilon (finite precision parameter)

full list of labelings

conc1,2 have larger default values. Remove these small testing values to
create output like those used in RESULTS.ipymb
GenVaspFiles(structure, conc1="100 200 5",conc2="1 5")

#### Examples

Ex.1
--------------------------------------------------------------------------

execute: python getStructures.py 'Binary or Ternary'

output: binary struct_enum.out for fcc,bcc, and hcp will be generated in
eam_'fcc/, bcc/, hcp'/'Binary or Ternary'/

Ex.2
---------------------------------------------------------------------------

execute: python getStructures.py Al Ti

output: Structures_AlTi/'fcc/,bcc/,hcp/'/vasp.num
if the files are left unchanged num will be 7 vasp POSCAR files: the first 2
and 5 chosen randomly from between 100-200

See Examples folder to compare your output file.

Ex.3
----------------------------------------------------------------------------

execute: python getStructures.py Al Co Ni

output: Structures_AlCoNi/'fcc/,bcc/,hcp/'/vasp.num
if the files are left unchanged num will be 7 vasp POSCAR files: the first 2
and 5 chosen randomly from between 100-200

See Examples folder to compare your output file.





 
