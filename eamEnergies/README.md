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



 