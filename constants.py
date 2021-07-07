import numpy as np
from scipy import constants

# Bessel functions
from scipy.special import j0, j1

# physics constants
m_e = constants.value('electron mass energy equivalent in MeV')
e = constants.e
c = constants.c
hc = constants.h*c /constants.nano /constants.eV # eV.nm

# LCLS lattice info
# from bmad LCLS lattice
# all markers along undulator where beam data is being saved
markers = ['BEGUNDH', 'MM3', 'PFILT1', 'DBMARK37', 'HXRSTART', 'MBLMH13', 'VVHXU13','MBLMH14','VVHXU14','MBLMH15',\
           'VVHXU15','MBLMH16','VVHXU16','MBLMH17','VVHXU17','MBLMH18','VVHXU18','MBLMH19','VVHXU19','MBLMH20',\
           'VVHXU20','MBLMH21','MBLMH22','VVHXU22','MBLMH23','VVHXU23','MBLMH24','VVHXU24','MBLMH25','VVHXU25',\
           'MBLMH26','VVHXU26','MBLMH27','VVHXU27','HXRSSBEG','HXRSSEND','MBLMH28','MBLMH29','VVHXU29','MBLMH30',\
           'VVHXU30','MBLMH31','VVHXU31','MBLMH32','VVHXU32','MBLMH33','VVHXU33','MBLMH34','VVHXU34','MBLMH35',\
           'VVHXU35','MBLMH36','VVHXU36','MBLMH37','VVHXU37','MBLMH38','VVHXU38','MBLMH39','VVHXU39','MBLMH40',\
           'VVHXU40','MBLMH41','VVHXU41','MBLMH42','VVHXU42','MBLMH43','VVHXU43','MBLMH44','VVHXU44','MBLMH45',\
           'MPHH','VVHXU45','MBLMH46','MUQH','VVHXU46','RWWAKE5H','HXRTERM']

# z along und
z = [0,0.261,0.261,0.261,0.355,3.819,4.279,7.832,8.292,11.845,12.304,15.857,16.317,19.87,20.33,23.883,24.342,27.895,
28.355,31.908,32.368,35.921,39.933,40.393,43.946,44.406,47.959,48.418,51.971,52.431,55.984,56.444,59.997,60.456,
60.586,63.958,64.009,68.022,68.482,72.035,72.494,76.047,76.507,80.06,80.52,84.073,84.532,88.085,88.545,92.098,
92.558,96.111,96.57,100.123,100.583,104.136,104.596,108.149,108.608,112.161,112.621,116.174,116.634,120.187,
120.646,124.199,124.659,128.212,128.672,132.225,132.575,132.684,136.237,136.33,136.697,152.837,152.837]#,155.747] 

# LCLS undulator parameters
I_A = 17045 # Alfven current [A]
# undulator params
K_u = 3.5 # typical value for LCLS 
lambda_u = 0.03 # m
k_u = 2*np.pi/lambda_u
L_u = 155 # from lattice. Other source: 131.747 # length in m
# coupling 
eta = K_u**2 / ( 4 + 2*K_u**2 )  
JJ = j0(eta) - j1(eta)