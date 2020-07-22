import os,sys
sys.path.append(os.getcwd())
from nthcircularprime import nthcircularprime
import pytest


@pytest.mark.parametrize('x, result',[
	(1, 2), (2, 3), (3, 5), (4, 7), (5,11),
	(6, 13), (7, 17), (8, 31), (9, 37), (10, 71), 
	(11, 73), (12, 79), (13, 97), (14, 113), (15, 131), 
	(16, 197), (17, 199), (18, 311), (19, 337), (20, 373), 
	(21, 719), (22, 733), (23, 919), (24, 971), (25, 991), 
	(26, 1193), (27, 1931), (28, 3119), (29, 3779), (30, 7793), 
	(31, 7937), (32, 9311), (33, 9377), (34, 11939), (35, 19391), 
	(36, 19937), (37, 37199), (38, 39119), (39, 71993), (40, 91193), 
	(41, 93719), (42, 93911), (43, 99371), (44, 193939), (45, 199933), 
	(46, 319993), (47, 331999), (48, 391939)
])

def test_nthcircularprime(x, result):
	assert nthcircularprime(x) == result
