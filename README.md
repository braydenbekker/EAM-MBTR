[![Build Status](https://travis-ci.org/braydenbekker/EAM-MBTR.svg?branch=master)](https://travis-ci.org/braydenbekker/EAM-MBTR)
[![codecov](https://codecov.io/gh/braydenbekker/EAM-MBTR/branch/master/graph/badge.svg)](https://codecov.io/gh/braydenbekker/EAM-MBTR)
## My Research Impact


Provide and extensive proof of concept for MBTR, MPT, and High-Thoughput methods
and there ability to make fast and accurate out-of sample predictions for binary, ternary and quaternary system.

#### abstract
-------------

One of the central problems in materials research is accurately predicting the properties of an alloy. Computational materials discovery has the potential to open the floodgates for human progression. Our society, built upon the materials discoveries of the past, lies in wait for the discovery of the next material that will change the world. 
\end{abstract}

#### Introduction
-----------------

In the past metallurgists made there discoveries through an exhaustive trial and error process which eventually resulted in a happy mistake. 

<img src="/ProgramFiles/RoyPlunkett.png" width="400">

Roy Plunkett was trying to create a new refrigerant when a buildup of a waxy material started to form on the inside of the container of CFC gasses he was working with. Teflon soon followed.
With computers came computational methods which remove much of the guess work, however, these modern processes of materials prediction are still too slow. 

<img src="/ProgramFiles/materialscooking.png" width="400">

Imagine for me a stocked pantry, to create a dessert by trial and error would be a time consuming disaster. A cookbook provides necessary directions. If you know the recipe than the desired result can be achieved. If you imagine now, a materials pantry stocked with every possible configuration of elements the number of combinations are infinite. The existing computational methods like DFT (Density Functional Theory) act as materials cookbooks. While the existing "materials cookbooks" remove the guess work they have a time consuming method for searching the "table of contents" to continue or example. DFT makes accurate predictions but at high computational cost.    


<img src="/ProgramFiles/MBTR.png" width="400">

My current research is with the recently proposed Many Body Tensor Representation (MBTR) for atomic systems. This machine learning approach uses the existing materials "cookbooks" to train and then make out-of-sample predictions. My project researches the ability of MBTR to replace the existing materials "cookbooks" using machine learning to predict new materials at a faster rate.

#### Main Objective
-------------------

- Search the Interatomic Potentials Repository for binary/ternary systems with EAM potentials

- Use Enumlib to get the derivative superstructures for each system

- For each system from FCC, BCC, and HCP choose 2500 derivative structures: the first 500 and 2000 additional structures from 10-12 atom cells.  

- Relax the atomic positions and compute energies per atom and enthalpy.

- Plot the convex hull and verify with AFLOW that results are similar (EAM potentials will not match results, here we are only looking for general similarities.)

- Save the data for each system to a HDF5 file for ease of data access.

- Use results to train and predict in MBTR

Full API Documentation available at: [github pages](https://github.com/braydenbekker/braydenbekker.github.io/blob/master/eamEnergies/html/index.html). 
